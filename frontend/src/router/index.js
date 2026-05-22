import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UploadView from '@/views/UploadView.vue'
import SummarizeView from '@/views/SummarizeView.vue'
import RegisterView from '@/views/RegisterView.vue'
import LoginView from '@/views/LoginView.vue'


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
      path:'/register',
      name:'register',
      component:RegisterView
    },{
      path:'/login',
      name:'login',
      component:LoginView
    }
  ],
})

export default router
