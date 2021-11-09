import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunch from '../views/TheLunch.vue'
import TheLotto from '../views/TheLotto.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'TheLunch',
    component: TheLunch
  },
  {
    path: '/lotto',
    name: 'TheLotto',
    component: TheLotto
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
