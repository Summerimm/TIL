<template>
  <div>
    <h2>1단계</h2>
    <div class="container">
      <router-link to="/ssafeed">
        <font-awesome-icon :icon="['fas', 'chevron-circle-left']" size="lg" />
      </router-link>
      <img src="@/assets/ssafling.png" alt="ssafeed" width="40%" height="40%">
      <router-link to="/ssaflossom">
        <font-awesome-icon :icon="['fas', 'chevron-circle-right']" size="lg"/>
      </router-link>
    </div>
    <h2>싸플링</h2>
  </div>
</template>

<script>
export default {
  name: 'SsaflingView',
}
</script>
