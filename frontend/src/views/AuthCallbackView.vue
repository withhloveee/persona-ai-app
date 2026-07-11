<template>
  <div></div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/chat'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

onMounted(() => {
  const token = route.query.token
  const user = route.query.user

  if (typeof token === 'string' && token) {
    authStore.login(token, typeof user === 'string' ? user : '')
    router.replace('/upload')
    return
  }

  router.replace('/login')
})
</script>
