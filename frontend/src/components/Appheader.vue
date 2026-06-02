<template>
  <header
    class="app-header"
    :class="{ 'sticky-header': sticky }"
  >

    <div class="container-fluid px-4">

      <div class="d-flex justify-content-between align-items-center px-5">

        <!-- LEFT -->
        <h5 class="site-title m-0">
          <router-link to="/" class="site-link"><h3 class="brand-logo">talk2learn</h3> </router-link>
        </h5>

        <!-- RIGHT -->
        <nav class="d-flex align-items-center gap-5">

        <button
          v-for="item in navItems"
          :key="item.label"
          class="nav-btn"
          :class="{ active: item.active }"
          @click="item.action"
        >
          <i
            v-if="item.icon"
            :class="`bi bi-${item.icon}`"
            class="me-2"
          ></i>

          {{ item.label }}
        </button>

          <button
            v-if="authStore.isLoggedIn"
            class="nav-btn"
            @click="logout"
          >
            <i class="bi bi-box-arrow-right me-2"></i>
            Logout
          </button>

        </nav>

      </div>

    </div>

  </header>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore,useSummaryStore  } from '@/stores/chat';
import { storeToRefs } from 'pinia';

const router = useRouter()

defineProps({
  navItems: {
    type: Array,
    default: () => []
  },

  sticky: {
    type: Boolean,
    default: true
  }
})

// for logout:
const authStore = useAuthStore()
const summaryStore = useSummaryStore()
const { messages,markdown } = storeToRefs(summaryStore)

function logout() {
  localStorage.removeItem('token')
  localStorage.removeItem('user')

  authStore.isLoggedIn = false
  messages.value = []
  markdown.value = ""

  router.push('/')
}

</script>

<style scoped>
.app-header {
  background: #FFFFFF;
  border-bottom: 1px solid #E5E7EB;
  padding: 16px 0;
  z-index: 1000;
}

.sticky-header {
  position: sticky;
  top: 0;
}

.site-title {
  font-weight: 700;
  color: #212529;
  letter-spacing: -0.5px;
}

/* NAV */

.nav-btn {
  border: none;
  background: transparent;
  padding: 0;
  color: #6c757d;
  font-size: 0.95rem;
  font-weight: 500;
  transition: color 0.18s ease;
}

.nav-btn:hover {
  color: #0d6efd;
}

.nav-btn.active {
  color: #0d6efd;
}

.site-link {
  color: inherit;
  text-decoration: none;
}

.site-link:hover {
  color: inherit;
}

.brand-logo {
  margin: 0;

  font-size: 1.72rem;
  font-weight: 700;

  color: #0d6efd;

  font-family:
    Inter,
    SF Pro Display,
    Segoe UI,
    sans-serif;

  letter-spacing: -1px;

  user-select: none;
}
</style>