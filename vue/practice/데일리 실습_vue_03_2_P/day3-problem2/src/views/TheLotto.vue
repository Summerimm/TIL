<template>
  <div>
    <h1>로또</h1>
    <button @click="getLottoNumbers">Get Lucky Numbers</button>
    <p>{{ lottoNumbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return {
      lottoNumbers: null,
    }
  },
  methods: {
    getLottoNumbers() {
      const numbers = _.sampleSize(_.range(1, 46), 6)
      this.lottoNumbers = numbers
    }
  }
}
</script>
