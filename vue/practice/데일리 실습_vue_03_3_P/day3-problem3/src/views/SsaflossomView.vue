<template>
  <div>
    <h2>2단계</h2>
    <div class="container">
      <router-link to="/ssafling">
        <font-awesome-icon :icon="['fas', 'chevron-circle-left']" size="lg" />
      </router-link>
      <img src="@/assets/ssaflossom.png" alt="ssafeed" width="40%" height="40%">
      <router-link to="/ssaflower">
        <font-awesome-icon :icon="['fas', 'chevron-circle-right']" size="lg"/>
      </router-link>
    </div>
    <h2>싸플라썸</h2>
  </div>
</template>

<script>
export default {
  name: 'SsaflossomView',
}
</script>
