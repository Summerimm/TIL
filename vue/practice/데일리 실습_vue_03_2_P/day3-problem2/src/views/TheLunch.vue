<template>
  <div>
    <div>
      <h1>점심메뉴</h1>
      <button @click="pickLunch">Pick Lunch</button>
      <p>{{ menu }}</p>
    </div>
    <br><br>
    <div>
      <h2>로또를 뽑아보자</h2>
      <router-link to="/lotto/6">
        <button>PickLotto</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data() {
    return {
      menuList: ['국밥', '떡볶이', '파스타', '샌드위치', '고기'],
      menu: null,
    }
  },
  methods: {
    pickLunch() {
      const menuNum = _.random(1, 5)
      this.menu = this.menuList[menuNum]
    },
    pickLotto() {
      // window.location.href = 'http://localhost:8080/lotto/6'
    }
  }

}
</script>

<style>

</style>