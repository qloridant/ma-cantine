<template>
  <div class="text-left">
    <BreadcrumbsNav :links="[{ to: { name: 'ManagementPage' } }]" />
    <h1 class="font-weight-black text-h4 mb-2">Actions en attente</h1>
    <p class="mt-0 mb-8">Concernant l'année {{ year }}</p>
    <AnnualActionableCanteensTable />
  </div>
</template>

<script>
import AnnualActionableCanteensTable from "./AnnualActionableCanteensTable"
import BreadcrumbsNav from "@/components/BreadcrumbsNav"
import { lastYear } from "@/utils"

export default {
  name: "PendingActions",
  components: { AnnualActionableCanteensTable, BreadcrumbsNav },
  data() {
    return {
      year: lastYear(),
    }
  },
}
</script>
