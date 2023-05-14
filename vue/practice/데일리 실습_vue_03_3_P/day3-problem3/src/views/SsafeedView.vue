<template>
  <div>
    <h2>시작</h2>
    <div class="container">
      <router-link to="/">
        <font-awesome-icon :icon="['fas', 'chevron-circle-left']" size="lg" />
      </router-link>
      <img src="@/assets/ssafeed.png" alt="ssafeed" width="40%" height="40%">
      <router-link to="/ssafling">
        <font-awesome-icon :icon="['fas', 'chevron-circle-right']" size="lg"/>
      </router-link>
    </div>
    <h2>싸피드</h2>
  </div>
</template>

<script>

export default {
  name: 'SsafeedView',
  components: {
  },
}
</script>
