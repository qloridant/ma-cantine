import csv
import time
import re
import logging
from decimal import Decimal
from data.models.diagnostic import Diagnostic
from django.db import IntegrityError, transaction
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from api.serializers import FullCanteenSerializer
from data.models import Canteen, Sector
from api.permissions import IsAuthenticated
from .utils import camelize, normalise_siret
from .canteen import AddManagerView
import requests

logger = logging.getLogger(__name__)


class ImportDiagnosticsView(APIView):
    permission_classes = [IsAuthenticated]
    value_error_regex = re.compile(r"Field '(.+)' expected .+? got '(.+)'.")
    annotated_sectors = Sector.objects.annotate(name_lower=Lower("name"))

    def __init__(self, **kwargs):
        self.diagnostics_created = 0
        self.canteens = {}
        self.errors = []
        self.start_time = None
        super().__init__(**kwargs)

    def post(self, request):
        self.start_time = time.time()
        logger.info("Diagnostic bulk import started")
        try:
            with transaction.atomic():
                file = request.data["file"]
                ImportDiagnosticsView._verify_file_size(file)
                self._treat_csv_file(file)

                if self.errors:
                    raise IntegrityError()
        except IntegrityError as e:
            logger.exception(e)
            logger.error("L'import du fichier CSV a échoué")
        except ValidationError as e:
            message = e.message
            logger.error(message)
            self.errors = [{"row": 0, "status": 400, "message": message}]
        except Exception as e:
            logger.exception(e)
            self.errors = [{"row": 0, "status": 400, "message": "Échec lors de la lecture du fichier"}]

        return self._get_success_response()

    @staticmethod
    def _verify_file_size(file):
        if file.size > settings.CSV_IMPORT_MAX_SIZE:
            raise ValidationError("Ce fichier est trop grand, merci d'utiliser un fichier de moins de 10Mo")

    def _treat_csv_file(self, file):
        locations_csv_str = "siret,citycode,postcode\n"
        has_locations_to_find = False

        filestring = file.read().decode("utf-8-sig")
        filelines = filestring.splitlines()
        dialect = csv.Sniffer().sniff(filelines[0])

        csvreader = csv.reader(filelines, dialect=dialect)
        for row_number, row in enumerate(csvreader, start=1):
            if self._skip_row(row_number, row):
                continue
            try:
                if row[0] == "":
                    raise ValidationError({"siret": "Le siret de la cantine ne peut pas être vide"})
                siret = normalise_siret(row[0])
                canteen, should_update_geolocation = self._update_or_create_canteen_with_diagnostic(row, siret)
                self.canteens[canteen.siret] = canteen
                if should_update_geolocation:
                    has_locations_to_find = True
                    if canteen.city_insee_code:
                        locations_csv_str += f"{canteen.siret},{canteen.city_insee_code},\n"
                    else:
                        locations_csv_str += f"{canteen.siret},,{canteen.postal_code}\n"

            except Exception as e:
                for error in self._parse_errors(e, row):
                    self.errors.append(
                        ImportDiagnosticsView._get_error(e, error["message"], error["code"], row_number)
                    )
        if has_locations_to_find:
            self._update_location_data(self.canteens, locations_csv_str)
        return (self.canteens, self.errors)

    # def _treat_csv_file(file):
    #     # read the file
    #     # for each row
    #     # basic format checks --- overriding
    #     # optionally skip headers --- overriding
    #     # validate canteen data, returning canteen
    #     # validate diagnostic data, returning diagnostic --- overriding
    #     # save canteen
    #     # save diagnostic
    #     pass

    @staticmethod
    def _should_update_geolocation(canteen, row):
        if canteen.city:
            city_code_changed = row[2] and canteen.city_insee_code != row[2].strip()
            postal_code_changed = row[3] and canteen.postal_code != row[3].strip()
            return city_code_changed or postal_code_changed
        else:
            has_geo_data = canteen.city_insee_code or canteen.postal_code
            return has_geo_data

    @staticmethod
    def _get_error(e, message, error_status, row_number):
        logger.error(f"Error on row {row_number}")
        logger.exception(e)
        return {"row": row_number, "status": error_status, "message": message}

    @staticmethod
    def _get_verbose_field_name(field_name):
        try:
            return Canteen._meta.get_field(field_name).verbose_name
        except:
            try:
                return Diagnostic._meta.get_field(field_name).verbose_name
            except:
                pass
        return field_name

    @staticmethod
    def _get_manager_emails(row):
        manager_emails = row.split(",")
        normalized_emails = list(map(lambda x: get_user_model().objects.normalize_email(x.strip()), manager_emails))
        for email in normalized_emails:
            validate_email(email)
        return normalized_emails

    @staticmethod
    def _add_managers_to_canteen(emails, canteen, send_invitation_mail=True):
        for email in emails:
            try:
                AddManagerView.add_manager_to_canteen(email, canteen, send_invitation_mail=send_invitation_mail)
            except IntegrityError as e:
                logger.error(
                    f"Attempt to add existing manager with email {email} to canteen {canteen.id} from a CSV import"
                )
                logger.exception(e)

    def _get_success_response(self):
        serialized_canteens = [camelize(FullCanteenSerializer(canteen).data) for canteen in self.canteens.values()]
        return JsonResponse(
            {
                "canteens": serialized_canteens,
                "count": 0 if len(self.errors) else self.diagnostics_created,
                "errors": self.errors,
                "seconds": time.time() - self.start_time,
            },
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def _update_location_data(canteens, locations_csv_str):
        try:
            # NB: max size of a csv file is 50 MB
            response = requests.post(
                "https://api-adresse.data.gouv.fr/search/csv/",
                files={
                    "data": ("locations.csv", locations_csv_str),
                },
                data={
                    "postcode": "postcode",
                    "citycode": "citycode",
                    "result_columns": ["result_citycode", "result_postcode", "result_city", "result_context"],
                },
                timeout=3,
            )
            response.raise_for_status()  # Raise an exception if the request failed
            for row in csv.reader(response.text.splitlines()):
                if row[0] == "siret":
                    continue  # skip header
                if row[5] != "":  # city found, so rest of data is found
                    canteen = canteens[row[0]]
                    canteen.city_insee_code = row[3]
                    canteen.postal_code = row[4]
                    canteen.city = row[5]
                    canteen.department = row[6].split(",")[0]
                    canteen.save()
        except Exception as e:
            logger.error(f"Error while updating location data : {repr(e)} - {e}")

    @staticmethod
    def _add_error(errors, message, code=400):
        errors.append({"message": message, "code": code})


# flake8: noqa: C901
class ImportSimpleDiagnosticsView(ImportDiagnosticsView):
    final_value_idx = 21
    manager_column_idx = 10
    year_idx = 11

    def _skip_row(self, row_number, row):
        return row_number == 1 and row[0].lower() == "siret"

    @transaction.atomic
    def _update_or_create_canteen_with_diagnostic(self, row, siret):
        # first check that the number of columns is good
        #   to throw error if badly formatted early on.
        # NB: if year is given, appro data is required, else only canteen data required
        # TODO: different number of columns if type is complete
        if len(row) > self.final_value_idx + 1 and not self.request.user.is_staff:
            raise PermissionDenied(
                detail=f"Format fichier : {self.final_value_idx + 1} ou 11 colonnes attendues, {len(row)} trouvées."
            )
        diagnostic_year = None
        try:
            diagnostic_year = row[self.year_idx]
            if not diagnostic_year and any(row[12 : self.final_value_idx]):
                raise ValidationError({"year": "L'année est obligatoire pour créer un diagnostic."})
        except IndexError:
            pass

        if diagnostic_year:
            row[self.final_value_idx]  # check all required diagnostic fields are given
        else:
            row[self.manager_column_idx - 1]  # managers are optional, so could be missing too

        if not row[5]:
            raise ValidationError({"daily_meal_count": "Ce champ ne peut pas être vide."})
        elif not row[2] and not row[3]:
            raise ValidationError(
                {"postal_code": "Ce champ ne peut pas être vide si le code INSEE de la ville est vide."}
            )

        try:
            manager_emails = []
            if len(row) > self.manager_column_idx + 1 and row[self.manager_column_idx]:
                manager_emails = ImportDiagnosticsView._get_manager_emails(row[self.manager_column_idx])
        except Exception as e:
            raise ValidationError({"email": "Un adresse email des gestionnaires n'est pas valide."})

        if diagnostic_year:
            value_fields = [
                "value_total_ht",
                "value_bio_ht",
                "value_sustainable_ht",
                "value_externality_performance_ht",
                "value_egalim_others_ht",
                "value_meat_poultry_ht",
                "value_meat_poultry_egalim_ht",
                "value_meat_poultry_france_ht",
                "value_fish_ht",
                "value_fish_egalim_ht",
            ]
            values_dict = {}
            value_offset = 0
            for value in value_fields:
                try:
                    value_offset = value_offset + 1
                    value_idx = self.year_idx + value_offset
                    if not row[value_idx]:
                        raise Exception
                    values_dict[value] = Decimal(row[value_idx].strip().replace(",", "."))
                except Exception as e:
                    error = {}
                    # TODO: This should take into account more number formats and be factored out to utils
                    error[value] = "Ce champ doit être un nombre décimal."
                    raise ValidationError(error)

        silent_manager_idx = self.final_value_idx + 1
        silently_added_manager_emails = []
        import_source = "Import massif"
        publication_status = Canteen.PublicationStatus.DRAFT
        if len(row) > silent_manager_idx:  # already checked earlier that it's a staff user
            try:
                if row[silent_manager_idx]:
                    silently_added_manager_emails = ImportDiagnosticsView._get_manager_emails(row[silent_manager_idx])
            except Exception as e:
                raise ValidationError(
                    {
                        "email": f"Un adresse email des gestionnaires (pas notifiés) ({row[silent_manager_idx]}) n'est pas valide."
                    }
                )

            try:
                import_source = row[silent_manager_idx + 1].strip()
            except Exception as e:
                raise ValidationError({"import_source": "Ce champ ne peut pas être vide."})

            status_idx = silent_manager_idx + 2
            if len(row) > status_idx and row[status_idx]:
                publication_status = row[status_idx].strip()

        canteen_exists = Canteen.objects.filter(siret=siret).exists()
        canteen = Canteen.objects.get(siret=siret) if canteen_exists else Canteen.objects.create(siret=siret)

        if canteen_exists and self.request.user not in canteen.managers.all():
            raise PermissionDenied(detail="Vous n'êtes pas un gestionnaire de cette cantine.")

        should_update_geolocation = (
            ImportDiagnosticsView._should_update_geolocation(canteen, row) if canteen_exists else True
        )

        canteen.name = row[1].strip()
        canteen.city_insee_code = row[2].strip()
        canteen.postal_code = row[3].strip()
        canteen.central_producer_siret = normalise_siret(row[4])
        canteen.daily_meal_count = row[5].strip()
        canteen.production_type = row[7].strip().lower()
        canteen.management_type = row[8].strip().lower()
        canteen.economic_model = row[9].strip().lower()
        canteen.import_source = import_source
        canteen.publication_status = publication_status

        # full_clean must be before the relation-model updates bc they don't require a save().
        # If an exception is launched by full_clean, it must be here.
        canteen.full_clean()
        if row[6]:
            canteen.sectors.set(
                [
                    self.annotated_sectors.get(name_lower__unaccent=sector.strip().lower())
                    for sector in row[6].split("+")
                ]
            )

        canteen.save()

        if not self.request.user.is_staff:
            canteen.managers.add(self.request.user)
        if manager_emails:
            ImportDiagnosticsView._add_managers_to_canteen(manager_emails, canteen)
        if silently_added_manager_emails:
            ImportDiagnosticsView._add_managers_to_canteen(
                silently_added_manager_emails, canteen, send_invitation_mail=False
            )

        if diagnostic_year:
            diagnostic = Diagnostic(
                canteen_id=canteen.id,
                year=diagnostic_year,
                value_total_ht=values_dict["value_total_ht"],
                value_bio_ht=values_dict["value_bio_ht"],
                value_sustainable_ht=values_dict["value_sustainable_ht"],
                value_externality_performance_ht=values_dict["value_externality_performance_ht"],
                value_egalim_others_ht=values_dict["value_egalim_others_ht"],
                value_meat_poultry_ht=values_dict["value_meat_poultry_ht"],
                value_meat_poultry_egalim_ht=values_dict["value_meat_poultry_egalim_ht"],
                value_meat_poultry_france_ht=values_dict["value_meat_poultry_france_ht"],
                value_fish_ht=values_dict["value_fish_ht"],
                value_fish_egalim_ht=values_dict["value_fish_egalim_ht"],
                diagnostic_type=Diagnostic.DiagnosticType.SIMPLE,
            )
            diagnostic.full_clean()
            diagnostic.save()
            self.diagnostics_created += 1
        return (canteen, should_update_geolocation)

    def _parse_errors(self, e, row):
        errors = []
        if isinstance(e, PermissionDenied):
            ImportDiagnosticsView._add_error(errors, e.detail, 401)
        elif isinstance(e, Sector.DoesNotExist):
            ImportDiagnosticsView._add_error(errors, "Le secteur spécifié ne fait pas partie des options acceptées")
        elif isinstance(e, ValidationError):
            if e.message_dict:
                for field, messages in e.message_dict.items():
                    verbose_field_name = ImportDiagnosticsView._get_verbose_field_name(field)
                    for message in messages:
                        user_message = message
                        if user_message == "Un objet Diagnostic avec ces champs Canteen et Année existe déjà.":
                            user_message = "Un diagnostic pour cette année et cette cantine existe déjà."
                        if field != "__all__":
                            user_message = f"Champ '{verbose_field_name}' : {user_message}"
                        ImportDiagnosticsView._add_error(errors, user_message)

            elif hasattr(e, "params"):
                ImportDiagnosticsView._add_error(errors, f"La valeur '{e.params['value']}' n'est pas valide.")
            else:
                ImportDiagnosticsView._add_error(
                    errors, "Une erreur s'est produite en créant un diagnostic pour cette ligne"
                )
        elif isinstance(e, ValueError):
            match = self.value_error_regex.search(str(e))
            field_name = match.group(1) if match else ""
            value_given = match.group(2) if match else ""
            if field_name:
                verbose_field_name = ImportDiagnosticsView._get_verbose_field_name(field_name)
                ImportDiagnosticsView._add_error(
                    errors, f"La valeur '{value_given}' n'est pas valide pour le champ '{verbose_field_name}'."
                )
        elif isinstance(e, IndexError):
            ImportDiagnosticsView._add_error(
                errors, f"Données manquantes : 22 colonnes attendues, {len(row)} trouvées."
            )
        elif isinstance(e, Canteen.MultipleObjectsReturned):
            ImportDiagnosticsView._add_error(
                errors,
                f"Plusieurs cantines correspondent au SIRET {row[0]}. Veuillez enlever les doublons pour pouvoir créer le diagnostic.",
            )
        if not errors:
            ImportDiagnosticsView._add_error(
                errors, "Une erreur s'est produite en créant un diagnostic pour cette ligne"
            )
        return errors


class ImportCompleteDiagnosticsView(ImportDiagnosticsView):
    permission_classes = [IsAuthenticated]
