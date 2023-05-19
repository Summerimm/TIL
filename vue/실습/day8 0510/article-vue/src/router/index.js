import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/', 
    name: 'IndexView',
    component: IndexView
  },
  {
    path: '/:id', 
    name: 'DetailView',
    component: () => import('../views/DetailView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
