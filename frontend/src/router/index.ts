import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import TripList from '../views/TripList.vue'
import TripForm from '../views/TripForm.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'TripList',
    component: TripList
  },
  {
    path: '/trip/new',
    name: 'NewTrip',
    component: TripForm
  },
  {
    path: '/trip/:id/edit',
    name: 'EditTrip',
    component: TripForm,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
