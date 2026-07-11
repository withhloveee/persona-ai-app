import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UploadView from '@/views/UploadView.vue'
import SummarizeView from '@/views/SummarizeView.vue'
import LoginView from '@/views/LoginView.vue'
import AboutView from '@/views/AboutView.vue'
import AuthCallbackView from '@/views/AuthCallbackView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path:'/upload',
      name:'upload',
      component: UploadView
    },
    {
      path:'/summarize',
      name:'summarize',
      component: SummarizeView
    },{
      path:'/login',
      name:'login',
      component:LoginView
    },{
      path:'/auth/callback',
      name:'auth-callback',
      component:AuthCallbackView
    },{
      path:'/about',
      name:'about',
      component:AboutView
    }
  ],
})

export default router
