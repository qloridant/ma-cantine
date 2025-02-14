<template>
  <v-list rounded class="text-left">
    <v-list-item-group active-class="menu-item--active">
      <div v-for="(item, index) in items" :key="index">
        <v-divider v-if="item.type === 'divider' && shouldDisplay(item)" class="my-2"></v-divider>
        <v-list-item
          v-else-if="shouldDisplay(item)"
          :to="item.to"
          :href="item.href"
          :ripple="false"
          :target="item.target"
          :rel="item.rel"
        >
          <v-list-item-title class="body-2">
            <v-icon small color="grey darken-2" class="mt-n1 mr-2">{{ item.icon }}</v-icon>
            {{ item.text }}
          </v-list-item-title>
        </v-list-item>
      </div>
      <v-divider v-if="loggedUser" class="my-2"></v-divider>
      <!-- logout button with warning -->
      <v-dialog v-if="loggedUser" v-model="logoutWarningDialog" max-width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-list-item :input-value="logoutWarningDialog" :ripple="false" v-bind="attrs" v-on="on">
            <v-list-item-title class="body-2">
              <v-icon small color="grey darken-2" class="mt-n1 mr-2">$logout-box-r-fill</v-icon>
              Me déconnecter
            </v-list-item-title>
          </v-list-item>
        </template>

        <v-card>
          <v-card-text class="pa-8 text-left">
            Voulez-vous vous déconnecter de votre compte ma cantine ?
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="grey darken-2" text @click="logoutWarningDialog = false" class="mr-1">
              Non, revenir en arrière
            </v-btn>
            <v-btn color="red darken-2" text href="/se-deconnecter">
              Oui, je confirme
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-list-item-group>
  </v-list>
</template>

<script>
export default {
  name: "HeaderDropdownList",
  data() {
    return {
      logoutWarningDialog: false,
      items: [
        {
          text: "Mes cantines",
          icon: "$layout-grid-fill",
          authenticationState: true,
          to: { name: "ManagementPage" },
        },
        {
          text: "Mes achats",
          icon: "mdi-food-apple",
          authenticationState: true,
          to: { name: "PurchasesHome" },
        },
        {
          text: "S'identifier",
          icon: "mdi-key",
          breakpoint: "smAndDown",
          authenticationState: false,
          href: "/s-identifier",
        },
        {
          text: "Créer un compte",
          icon: "$account-circle-fill",
          breakpoint: "smAndDown",
          authenticationState: false,
          href: "/creer-mon-compte",
        },
        {
          text: "Autodiagnostic",
          icon: "mdi-chart-pie",
          authenticationState: false,
          to: { name: "DiagnosticPage" },
        },
        {
          text: "Générer mon affiche",
          icon: "$article-fill",
          to: { name: "GeneratePosterPage" },
        },
        {
          text: "Mon profil",
          icon: "$account-circle-fill",
          authenticationState: true,
          to: { name: "AccountSummaryPage" },
        },
        {
          type: "divider",
        },
        {
          text: "Mesures phares",
          icon: "$line-chart-fill",
          to: { name: "KeyMeasuresHome" },
        },
        {
          text: "Nos cantines",
          icon: "$restaurant-fill",
          to: { name: "CanteensHome" },
        },
        {
          text: "Webinaires",
          icon: "$team-fill",
          to: { name: "CommunityPage" },
        },
        {
          text: "Acteurs de l'éco-système",
          icon: "$star-fill",
          to: { name: "PartnersHome" },
        },
        {
          text: "Blog",
          icon: "$newspaper-fill",
          to: { name: "BlogsHome" },
        },
        {
          text: "Documentation",
          icon: "$book-2-fill",
          href: "https://ma-cantine-1.gitbook.io/ma-cantine-egalim/",
          target: "_blank",
          rel: "noopener",
        },
        {
          type: "divider",
        },
        {
          text: "Les cantines dans ma collectivité",
          icon: "$france-fill",
          to: { name: "PublicCanteenStatisticsPage" },
        },
        {
          text: "Mesures de notre impact",
          icon: "$bar-chart-box-fill",
          to: { name: "ImpactMeasuresPage" },
        },
        {
          text: "Foire aux questions",
          icon: "$question-answer-fill",
          to: { name: "FaqPage" },
        },
        {
          text: "Contactez-nous",
          icon: "$question-fill",
          to: { name: "ContactPage" },
        },
      ],
    }
  },
  computed: {
    loggedUser() {
      return this.$store.state.loggedUser
    },
  },
  methods: {
    shouldDisplay(item) {
      if (item.authenticationState === true && !this.loggedUser) return false
      if (item.authenticationState === false && this.loggedUser) return false
      if (item.breakpoint && !this.$vuetify.breakpoint[item.breakpoint]) return false
      return true
    },
  },
}
</script>

<style scoped>
.v-list--rounded .v-list-item,
.v-list--rounded .v-list-item::before,
.v-list--rounded .v-list-item > .v-ripple__container {
  border-radius: 12px !important;
}
</style>
