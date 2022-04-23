import { createRouter, createWebHistory } from 'vue-router'
import SelectLocation from '../views/SelectLocation.vue'
import StartGame from '../views/StartGame.vue'
import PlayGame from '../views/PlayGame.vue'

const routes = [
  {
    path: '/',
    name: 'SelectLocation',
    component: SelectLocation
  },
  {
    path: '/startGame',
    name: 'startGame',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: StartGame
  },
  {
    path: '/playGame',
    name: 'playGame',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: PlayGame
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
