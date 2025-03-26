import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CalendarView from '../views/CalendarView.vue'
import SignupForm from "@/views/SignupForm.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/sign-up',
      name: 'signUp',
      component: SignupForm
    },
    {
      path: '/calendar',
      name: 'calendar',
      component: CalendarView,
      beforeEnter: () => {
        return !!localStorage.getItem('user');
      }
    }
  ],
})

export default router
