export default Object.freeze({
  LoadingStatus: {
    LOADING: 1,
    SUCCESS: 2,
    ERROR: 3,
    IDLE: 4,
  },
  DefaultDiagnostics: {
    id: null,
    year: null,
    valueBioHt: null,
    valueSustainableHt: null,
    valueTotalHt: null,
    hasWasteDiagnostic: null,
    hasWastePlan: null,
    wasteActions: [],
    hasDonationAgreement: null,
    hasDiversificationPlan: null,
    vegetarianWeeklyRecurrence: null,
    vegetarianMenuType: null,
    vegetarianMenuBases: [],
    cookingPlasticSubstituted: null,
    servingPlasticSubstituted: null,
    plasticBottlesSubstituted: null,
    plasticTablewareSubstituted: null,
    communicationSupports: [],
    communicationSupportUrl: null,
    communicatesOnFoodPlan: null,
  },
  ManagementTypes: [
    {
      text: "Directe",
      value: "direct",
    },
    {
      text: "Concédée",
      value: "conceded",
    },
  ],
  ProductionTypes: [
    {
      text: "Cuisines centrales",
      value: "central,central_serving",
    },
    {
      text: "Cantines satellites et autogérées",
      value: "site,site_cooked_elsewhere",
    },
  ],
  ProductionTypesDetailed: [
    {
      title: "produit sur place les repas qu'il sert à ses convives",
      body: "Mon établissement prépare ce qu'il sert à ses convives",
      value: "site",
    },
    {
      title: "sert des repas preparés par un autre établissement",
      body: "Les repas que mon établissement sert à ses convives sont cuisinés ailleurs",
      value: "site_cooked_elsewhere",
    },
    {
      title: "livre des repas mais n'a pas de lieu de service en propre",
      body: "Mon établissement livre des repas mais n'a pas de lieu de service en propre",
      value: "central",
    },
    {
      title: "livre des repas et accueille aussi des convives sur place",
      body: "Mon établissement livre des repas et accueille aussi des convives sur place",
      value: "central_serving",
    },
  ],
  EconomicModels: [
    { text: "Public", value: "public" },
    { text: "Privé", value: "private" },
  ],
  ProductFamilies: {
    VIANDES_VOLAILLES: {
      text: "Viandes et volailles fraîches et surgelées",
      shortText: "viandes et volailles",
      color: "pink darken-4",
    },
    CHARCUTERIE: {
      text: "Charcuterie",
      shortText: "charcuterie",
      color: "pink darken-4",
    },
    PRODUITS_DE_LA_MER: {
      text: "Produits aquatiques frais et surgelés",
      shortText: "produits aquatiques",
      color: "blue darken-3",
    },
    FRUITS_ET_LEGUMES: {
      text: "Fruits et légumes frais et surgelés",
      shortText: "fruits et légumes",
      color: "green darken-3",
    },
    PRODUITS_LAITIERS: {
      text: "BOF (Produits laitiers, beurre et œufs)",
      shortText: "BOF",
      color: "deep-orange darken-4",
    },
    BOULANGERIE: {
      text: "Boulangerie / Pâtisserie fraîches",
      shortText: "boulangerie / pâtisserie",
      color: "deep-purple darken-3",
    },
    BOISSONS: {
      text: "Boissons",
      shortText: "boissons",
      color: "green darken-4",
    },
    AUTRES: {
      text: "Autres produits frais, surgelés et d’épicerie",
      shortText: "autres produits",
      color: "grey darken-3",
    },
  },
  Characteristics: {
    // NB: the order of these keys reflects the priority of the label in EGAlim sum calculations
    // NB: the order of these can affect the aesthetics of the display on PurchasePage, esp for long texts
    BIO: { text: "Bio" },
    LABEL_ROUGE: { text: "Label rouge" },
    AOCAOP: { text: "AOC / AOP", longText: "Appellation d'origine (AOC / AOP)" },
    ICP: { text: "IGP", longText: "Indication géographique protégée (IGP)" },
    STG: { text: "STG", longText: "Spécialité traditionnelle garantie (STG)" },
    HVE: { text: "HVE", longText: "Certification environnementale de niveau 2 ou HVE" },
    PECHE_DURABLE: { text: "Écolabel pêche durable" },
    RUP: { text: "RUP", longText: "Région ultrapériphérique (RUP)" },
    COMMERCE_EQUITABLE: { text: "Commerce équitable" },
    FERMIER: { text: "Fermier", longText: "Mention « fermier » ou « produit de la ferme » ou « produit à la ferme »" },
    EXTERNALITES: {
      text: "Externalités environnementales",
      longText:
        "Produits acquis prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie",
    },
    PERFORMANCE: {
      text: "Performance environnementale",
      longText: "Produits acquis sur la base de leurs performances en matière environnementale",
    },
    FRANCE: { text: "Provenance France" },
    SHORT_DISTRIBUTION: { text: "Circuit-court" },
    LOCAL: { text: "Local" },
  },
  TeledeclarationCharacteristics: {
    // NB: the order of these can affect the aesthetics of the display on PurchasePage, esp for long texts
    BIO: { text: "Bio", color: "green" },
    LABEL_ROUGE: { text: "Label rouge", color: "red lighten-1" },
    AOCAOP_IGP_STG: {
      text: "AOC / AOP / IGP / STG",
      longText: "AOC / AOP / IGP / STG",
      color: "indigo",
    },
    PECHE_DURABLE: { text: "Écolabel pêche durable", color: "blue" },
    RUP: { text: "RUP", longText: "Région ultrapériphérique (RUP)", color: "brown" },
    COMMERCE_EQUITABLE: { text: "Commerce équitable", color: "lime darken-2" },
    HVE: {
      text: "Certification environnementale de niveau 2 ou HVE",
      longText: "Certification environnementale de niveau 2 ou HVE",
      color: "purple",
    },
    FERMIER: {
      text: "Fermier",
      longText: "Mention « fermier » ou « produit de la ferme » ou « produit à la ferme »",
      color: "orange",
    },
    EXTERNALITES: {
      text: "Externalités environnementales",
      longText:
        "Produits acquis prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie",
      color: "teal",
    },
    PERFORMANCE: {
      text: "Performance environnementale",
      longText: "Produits acquis sur la base de leurs performances en matière environnementale",
      color: "pink",
    },
    NON_EGALIM: { text: "Non-EGAlim", color: "blue-grey lighten-2" },
    FRANCE: { text: "Provenance France", additional: true },
    SHORT_DISTRIBUTION: { text: "Circuit-court", additional: true },
    LOCAL: { text: "Local", additional: true },
  },
  LocalDefinitions: {
    AUTOUR_SERVICE: { text: "200 km autour du lieu de service", value: "AUTOUR_SERVICE" },
    DEPARTMENT: { text: "Provenant du même département", value: "DEPARTMENT" },
    REGION: { text: "Provenant de la même région", value: "REGION" },
    AUTRE: { text: "Autre", value: "AUTRE" },
  },
  TeledeclarationCharacteristicGroups: {
    egalim: {
      text:
        "Pour la saisie, vous ne devez affecter le produit qu'une dans une seule catégorie. Par exemple, un produit à la fois biologique et label rouge sera comptabilisé que dans la catégorie 'bio'.",
      characteristics: [
        "BIO",
        "LABEL_ROUGE",
        "AOCAOP_IGP_STG",
        "HVE",
        "PECHE_DURABLE",
        "RUP",
        "COMMERCE_EQUITABLE",
        "FERMIER",
        "EXTERNALITES",
        "PERFORMANCE",
      ],
      fields: [
        "valueViandesVolaillesBio",
        "valueProduitsDeLaMerBio",
        "valueFruitsEtLegumesBio",
        "valueCharcuterieBio",
        "valueProduitsLaitiersBio",
        "valueBoulangerieBio",
        "valueBoissonsBio",
        "valueAutresBio",
        "valueViandesVolaillesLabelRouge",
        "valueProduitsDeLaMerLabelRouge",
        "valueFruitsEtLegumesLabelRouge",
        "valueCharcuterieLabelRouge",
        "valueProduitsLaitiersLabelRouge",
        "valueBoulangerieLabelRouge",
        "valueBoissonsLabelRouge",
        "valueAutresLabelRouge",
        "valueViandesVolaillesAocaopIgpStg",
        "valueProduitsDeLaMerAocaopIgpStg",
        "valueFruitsEtLegumesAocaopIgpStg",
        "valueCharcuterieAocaopIgpStg",
        "valueProduitsLaitiersAocaopIgpStg",
        "valueBoulangerieAocaopIgpStg",
        "valueBoissonsAocaopIgpStg",
        "valueAutresAocaopIgpStg",
        "valueViandesVolaillesHve",
        "valueProduitsDeLaMerHve",
        "valueFruitsEtLegumesHve",
        "valueCharcuterieHve",
        "valueProduitsLaitiersHve",
        "valueBoulangerieHve",
        "valueBoissonsHve",
        "valueAutresHve",
        "valueViandesVolaillesPecheDurable",
        "valueProduitsDeLaMerPecheDurable",
        "valueFruitsEtLegumesPecheDurable",
        "valueCharcuteriePecheDurable",
        "valueProduitsLaitiersPecheDurable",
        "valueBoulangeriePecheDurable",
        "valueBoissonsPecheDurable",
        "valueAutresPecheDurable",
        "valueViandesVolaillesRup",
        "valueProduitsDeLaMerRup",
        "valueFruitsEtLegumesRup",
        "valueCharcuterieRup",
        "valueProduitsLaitiersRup",
        "valueBoulangerieRup",
        "valueBoissonsRup",
        "valueAutresRup",
        "valueViandesVolaillesFermier",
        "valueProduitsDeLaMerFermier",
        "valueFruitsEtLegumesFermier",
        "valueCharcuterieFermier",
        "valueProduitsLaitiersFermier",
        "valueBoulangerieFermier",
        "valueBoissonsFermier",
        "valueAutresFermier",
        "valueViandesVolaillesExternalites",
        "valueProduitsDeLaMerExternalites",
        "valueFruitsEtLegumesExternalites",
        "valueCharcuterieExternalites",
        "valueProduitsLaitiersExternalites",
        "valueBoulangerieExternalites",
        "valueBoissonsExternalites",
        "valueAutresExternalites",
        "valueViandesVolaillesCommerceEquitable",
        "valueProduitsDeLaMerCommerceEquitable",
        "valueFruitsEtLegumesCommerceEquitable",
        "valueCharcuterieCommerceEquitable",
        "valueProduitsLaitiersCommerceEquitable",
        "valueBoulangerieCommerceEquitable",
        "valueBoissonsCommerceEquitable",
        "valueAutresCommerceEquitable",
        "valueViandesVolaillesPerformance",
        "valueProduitsDeLaMerPerformance",
        "valueFruitsEtLegumesPerformance",
        "valueCharcuteriePerformance",
        "valueProduitsLaitiersPerformance",
        "valueBoulangeriePerformance",
        "valueBoissonsPerformance",
        "valueAutresPerformance",
      ],
    },
    nonEgalim: {
      text: "Merci de renseigner les montants des produits hors EGAlim",
      characteristics: ["NON_EGALIM"],
      fields: [
        "valueViandesVolaillesNonEgalim",
        "valueProduitsDeLaMerNonEgalim",
        "valueFruitsEtLegumesNonEgalim",
        "valueCharcuterieNonEgalim",
        "valueProduitsLaitiersNonEgalim",
        "valueBoulangerieNonEgalim",
        "valueBoissonsNonEgalim",
        "valueAutresNonEgalim",
      ],
    },
    outsideLaw: {
      text:
        "Ici, vous pouvez affecter le produit dans plusieurs caractéristiques. Par exemple, un produit à la fois biologique et local pourra être comptabilisé dans les deux champs 'bio' et 'local'.",
      characteristics: ["FRANCE", "SHORT_DISTRIBUTION", "LOCAL"],
      fields: [
        "valueViandesVolaillesFrance",
        "valueProduitsDeLaMerFrance",
        "valueFruitsEtLegumesFrance",
        "valueCharcuterieFrance",
        "valueProduitsLaitiersFrance",
        "valueBoulangerieFrance",
        "valueBoissonsFrance",
        "valueAutresFrance",
        "valueViandesVolaillesShortDistribution",
        "valueProduitsDeLaMerShortDistribution",
        "valueFruitsEtLegumesShortDistribution",
        "valueCharcuterieShortDistribution",
        "valueProduitsLaitiersShortDistribution",
        "valueBoulangerieShortDistribution",
        "valueBoissonsShortDistribution",
        "valueAutresShortDistribution",
        "valueViandesVolaillesLocal",
        "valueProduitsDeLaMerLocal",
        "valueFruitsEtLegumesLocal",
        "valueCharcuterieLocal",
        "valueProduitsLaitiersLocal",
        "valueBoulangerieLocal",
        "valueBoissonsLocal",
        "valueAutresLocal",
      ],
    },
  },
  TrackingParams: ["mtm_source", "mtm_campaign", "mtm_medium"],
  Jobs: [
    {
      text: "Gestionnaire d'établissement",
      value: "ESTABLISHMENT_MANAGER",
    },
    {
      text: "Direction achat société de restauration",
      value: "CATERING_PURCHASES_MANAGER",
    },
    {
      text: "Responsable d'achats en gestion directe",
      value: "DIRECT_PURCHASES_MANAGER",
    },
    {
      text: "Responsable de plusieurs établissements (type cuisine centrale)",
      value: "CENTRAL_MANAGER",
    },
    {
      text: "Responsable de plusieurs établissements (SRC)",
      value: "MANY_ESTABLISHMENTS_MANAGER",
    },
    {
      text: "Développement logiciel, analyse de données ou autre rôle technique",
      value: "TECHNICAL",
    },
    {
      text: "Autre (spécifiez)",
      value: "OTHER",
    },
  ],
  UserSources: [
    {
      text: "Webinaire",
      value: "WEBINAIRE",
    },
    {
      text: "Recherche web",
      value: "WEB_SEARCH",
    },
    {
      text: "Communication institutionnelle (DRAAF, association régionale)",
      value: "INSTITUTION",
    },
    {
      text: "Bouche à oreille",
      value: "WORD_OF_MOUTH",
    },
    {
      text: "Réseaux sociaux",
      value: "SOCIAL_MEDIA",
    },
    {
      text: "Autre (spécifiez)",
      value: "OTHER",
    },
  ],
  SitemapGroups: {
    LAW: {
      label: "S'informer sur les lois",
    },
    DIAG: {
      label: "Se diagnostiquer",
    },
    ACTION: {
      label: "Améliorer votre offre",
    },
    SITE: {
      label: "Informations sur le site",
    },
  },
  DiagnosticImportLevels: [
    {
      key: "NONE",
      urlSlug: "cantines-seules",
      title: "Importer des cantines sans diagnostic",
      label: "Sans diagnostic",
      help: "Vous voulez importer des cantines sans données d'approvisionnement",
      icon: "$community-fill",
    },
    {
      key: "SIMPLE",
      urlSlug: "cantines-et-diagnostics-simples",
      title: "Importer des cantines et diagnostics simples",
      label: "Diagnostic simple",
      help: "Vous connaissez les valeurs totaux, bio, et de qualité et durable",
      icon: "$bar-chart-box-fill",
    },
    {
      key: "COMPLETE",
      urlSlug: "cantines-et-diagnostics-complets",
      title: "Importer des cantines et diagnostics complets",
      label: "Diagnostic complet",
      help: "Vous connaissez les labels et les familles de produits de vos achats",
      icon: "$checkbox-circle-fill",
    },
  ],
  MiscLabelIcons: {
    FERMIER: {
      icon: "mdi-cow",
      color: "brown",
    },
    EXTERNALITES: {
      icon: "mdi-flower-tulip-outline",
      color: "purple",
    },
    PERFORMANCE: {
      icon: "mdi-chart-line",
      color: "green",
    },
    NON_EGALIM: {
      icon: "mdi-dots-horizontal",
      color: "grey",
    },
    FRANCE: {
      icon: "$france-line",
      color: "indigo",
    },
    SHORT_DISTRIBUTION: {
      icon: "mdi-chart-timeline-variant",
      color: "pink",
    },
    LOCAL: {
      icon: "mdi-map-marker-outline",
      color: "blue",
    },
  },
  Ministries: [
    { value: "premier_ministre", text: "Service du Premier Ministre" },
    { value: "affaires_etrangeres", text: "Ministère de l’Europe et des Affaires étrangères" },
    { value: "ecologie", text: "Ministère de la Transition écologique" },
    { value: "jeunesse", text: "Ministère de l’Education Nationale et de la Jeunesse et des Sports" },
    { value: "economie", text: "Ministère de l’Economie, de la Finance et de la Relance" },
    { value: "armee", text: "Ministère de l’Armée" },
    { value: "interieur", text: "Ministère de l’Intérieur" },
    { value: "travail", text: "Ministère Travail, de l’Emploi et de l’Insertion" },
    { value: "outre_mer", text: "Ministère des Outre-mer" },
    {
      value: "territoires",
      text: "Ministère de la Cohésion des Territoires et des Relations avec les Collectivités Territoriales",
    },
    { value: "justice", text: "Ministère de la Justice" },
    { value: "culture", text: "Ministère de la Culture" },
    { value: "sante", text: "Ministère des Solidarités et de la Santé" },
    { value: "mer", text: "Ministère de la Mer" },
    {
      value: "enseignement_superieur",
      text: "Ministère de l’Enseignement Supérieur et de la Recherche et de l’Innovation",
    },
    { value: "agriculture", text: "Ministère de l’Agriculture et de l’Alimentation" },
    { value: "transformation", text: "Ministère de la Transformation et de la Fonction Publiques" },
    { value: "autre", text: "Autre" },
  ],
  CentralKitchenDiagnosticModes: [
    {
      key: "ALL",
      label: "Je rentre les données concernant toutes les mesures EGAlim pour mes cantines satellites",
    },
    {
      key: "APPRO",
      label: "Je rentre seulement les données d'approvisionnement pour mes cantines satellites",
    },
  ],
  SectorCategoryTranslations: {
    education: "Enseignement",
    health: "Santé",
    autres: "Autre",
    social: "Social et Médico-Social",
    administration: "Administration",
    leisure: "Loisirs",
    enterprise: "Entreprise",
    inconnu: "Inconnu",
  },
})
