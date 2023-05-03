<template>
  <div>
    <p>연봉 입력 (만원): <input v-model.number="salary" type="number"></p>
    <p>세액감면액 입력 (만원): <input v-model.number="tax" type="number"></p>
    <hr>
  </div>
</template>
<script>
import TaxrateComponent from './components/TaxrateComponent.vue'
export default {
  name: 'IncomeComponent',
  components: {
    TaxrateComponent,
  },
  data() => {
    salary:
  },

}
</script>

<style>

</style>