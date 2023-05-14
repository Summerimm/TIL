<template>
  <div>
    <h2>3단계</h2>
    <div class="container">
      <router-link to="/ssaflossom">
        <font-awesome-icon :icon="['fas', 'chevron-circle-left']" size="lg" />
      </router-link>
      <img src="@/assets/ssaflower.png" alt="ssafeed" width="40%" height="40%">
      <router-link to="/">
        <font-awesome-icon :icon="['fas', 'chevron-circle-right']" size="lg" @click="goHome"/>
      </router-link>
    </div>
    <h2>싸플라워</h2>
  </div>
</template>

<script>
export default {
  name: 'SsaflowerView',
  methods: {
    goHome() {
      alert('Home으로 돌아갑니다!')
    }
  }
}
</script>
