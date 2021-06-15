from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from data.factories import CanteenFactory, DiagnosticFactory
from data.models import Diagnostic
from .utils import authenticate
import decimal


class TestDiagnosticsApi(APITestCase):
    def test_unauthenticated_create_diagnostic_call(self):
        """
        When calling this API unathenticated we expect a 403
        """
        canteen = CanteenFactory.create()
        response = self.client.post(
            reverse("diagnostic_creation", kwargs={"canteen_pk": canteen.id}), {}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @authenticate
    def test_diagnostic_missing_canteen(self):
        """
        When calling this API on an unexistent canteen we expect a 404
        """
        response = self.client.post(
            reverse("diagnostic_creation", kwargs={"canteen_pk": 999}), {}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @authenticate
    def test_diagnostic_forbidden_canteen(self):
        """
        When calling this API on a canteen that the user doesn't manage,
        we expect a 403
        """
        canteen = CanteenFactory.create()
        response = self.client.post(
            reverse("diagnostic_creation", kwargs={"canteen_pk": canteen.id}), {}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @authenticate
    def test_create_diagnostic(self):
        """
        When calling this API on a canteen that the user manages
        we expect a diagnostic to be created
        """
        canteen = CanteenFactory.create()
        canteen.managers.add(authenticate.user)

        payload = {
            "year": 2020,
            "value_bio_ht": 1000,
            "value_fair_trade_ht": 2000,
            "value_sustainable_ht": 3000,
            "value_total_ht": 10000,
            "has_waste_diagnostic": True,
            "has_waste_plan": False,
            "waste_actions": ["INSCRIPTION", "AWARENESS"],
            "other_waste_action": "We compost things",
            "has_donation_agreement": False,
            "has_waste_measures": True,
            "bread_leftovers": 10.1,
            "served_leftovers": 20.2,
            "unserved_leftovers": 30.3,
            "side_leftovers": 40.4,
            "donation_frequency": 50,
            "donation_quantity": 60.6,
            "donation_food_type": "We donate bread and cheese",
            "other_waste_comments": "We do our best",
            "has_diversification_plan": True,
            "vegetarian_weekly_recurrence": "LOW",
            "vegetarian_menu_type": "UNIQUE",
            "vegetarian_menu_bases": ["GRAIN", "READYMADE"],
            "cooking_plastic_substituted": True,
            "serving_plastic_substituted": False,
            "plastic_bottles_substituted": True,
            "plastic_tableware_substituted": False,
            "communication_supports": ["DISPLAY", "DIGITAL"],
            "other_communication_support": "We put on plays",
            "communication_support_url": "https://example.com",
            "communicates_on_food_plan": True,
            "communicates_on_food_quality": True,
            "communication_frequency": "YEARLY",
        }
        response = self.client.post(
            reverse("diagnostic_creation", kwargs={"canteen_pk": canteen.id}), payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        diagnostic = Diagnostic.objects.get(canteen__id=canteen.id)

        self.assertEqual(diagnostic.year, 2020)
        self.assertTrue(diagnostic.cooking_plastic_substituted)
        self.assertFalse(diagnostic.has_donation_agreement)
        self.assertIn("AWARENESS", diagnostic.waste_actions)
        self.assertIn("GRAIN", diagnostic.vegetarian_menu_bases)
        self.assertEqual(diagnostic.donation_quantity, decimal.Decimal("60.6"))
        self.assertEqual(diagnostic.communication_frequency, "YEARLY")
        self.assertTrue(diagnostic.communicates_on_food_quality)

    @authenticate
    def test_edit_diagnostic_unauthorized(self):
        """
        The user can only edit diagnostics of canteens they
        manage
        """
        diagnostic = DiagnosticFactory.create()
        payload = {"year": 2020}

        response = self.client.patch(
            reverse(
                "diagnostic_edition",
                kwargs={"canteen_pk": diagnostic.canteen.id, "pk": diagnostic.id},
            ),
            payload,
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @authenticate
    def test_edit_diagnostic(self):
        """
        The user can edit a diagnostic of a canteen they manage
        """
        diagnostic = DiagnosticFactory.create(year=2019)
        diagnostic.canteen.managers.add(authenticate.user)
        payload = {"year": 2020}

        response = self.client.patch(
            reverse(
                "diagnostic_edition",
                kwargs={"canteen_pk": diagnostic.canteen.id, "pk": diagnostic.id},
            ),
            payload,
        )
        diagnostic.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(diagnostic.year, 2020)
