import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SsafeedView from '../views/SsafeedView.vue'
import SsaflingView from '../views/SsaflingView.vue'
import SsaflossomView from '../views/SsaflossomView.vue'
import SsaflowerView from '../views/SsaflowerView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/ssafeed',
    name: 'ssafeed',
    component: SsafeedView,
    beforeEnter(to, from, next) {
      if (from.path === '/') {
        next()
      } else {
        alert('이전 진화 단계로 돌아갈 수 없습니다.')
        next(from)
      }
    }
  },
  {
    path: '/ssafling',
    name: 'ssafling',
    component: SsaflingView
  },
  {
    path: '/ssaflossom',
    name: 'ssaflossom',
    component: SsaflossomView
  },
  {
    path: '/ssaflower',
    name: 'ssaflower',
    component: SsaflowerView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
