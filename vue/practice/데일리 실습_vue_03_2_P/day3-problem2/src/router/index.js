import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunch from '@/views/TheLunch.vue'
import TheLotto from '@/views/TheLotto.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: TheLunch
  },
  {
    path: '/lotto/6',
    name: 'lotto',
    component: TheLotto
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
