<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="SSAFY 여러분을 응원합니다!"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      msg: '이곳은 App.vue 입니다'
    }
  },
  props: {
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
