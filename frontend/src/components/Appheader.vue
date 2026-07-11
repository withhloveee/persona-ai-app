<template>
  <header
    class="app-header"
    :class="{ 'sticky-header': sticky }"
  >

    <div class="container-fluid header-container">

      <div class="nav-shell">

        <!-- LEFT -->
        <h5 class="site-title m-0">
          <router-link to="/" class="site-link">
            <h3 class="brand-logo">Talk2learn</h3>
          </router-link>
        </h5>

        <!-- RIGHT -->
        <nav class="nav-actions" aria-label="Primary navigation">

        <button
          v-for="item in navItems"
          :key="item.label"
          type="button"
          class="nav-btn"
          :class="{ active: item.active }"
          :aria-current="item.active ? 'page' : undefined"
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
            type="button"
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
  authStore.logout()
  messages.value = []
  markdown.value = ""

  router.push('/')
}

</script>

<style scoped>
.app-header {
  background: rgba(255, 255, 255, 0.96);
  border-bottom: 1px solid var(--app-border);
  box-shadow: 0 2px 14px rgba(20, 33, 61, 0.06);
  padding: 0;
  z-index: 1000;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.sticky-header {
  position: sticky;
  top: 0;
}

.header-container {
  padding-inline: clamp(1rem, 4vw, 4rem);
}

.nav-shell {
  width: min(100%, 1180px);
  min-height: 4.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  margin: 0 auto;
  padding: 0.45rem 0;
}

.site-title {
  font-weight: 700;
  color: #212529;
  letter-spacing: -0.5px;
  flex: 0 0 auto;
}

/* NAV */

.nav-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.nav-btn {
  position: relative;
  border: none;
  border-radius: 0.55rem;
  background: transparent;
  padding: 0.6rem 0.8rem;
  color: var(--app-muted);
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1;
  transition:
    background-color 0.18s ease,
    color 0.18s ease;
}

.nav-btn:hover,
.nav-btn:focus-visible {
  background: rgba(36, 84, 214, 0.07);
  color: var(--app-primary);
}

.nav-btn.active {
  background: rgba(36, 84, 214, 0.08);
  color: var(--app-primary);
}

.nav-btn:focus-visible {
  outline: 3px solid rgba(36, 84, 214, 0.22);
  outline-offset: 2px;
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

  font-size: clamp(1.25rem, 2vw, 1.72rem);
  font-weight: 700;

  color: var(--app-ink);
  font-family: "Geist Mono", monospace;

  letter-spacing: -1px;

  user-select: none;
}

@media (max-width: 767.98px) {
  .nav-shell {
    min-height: auto;
    align-items: flex-start;
    flex-direction: column;
    gap: 0.65rem;
    padding: 0.85rem 0;
  }

  .nav-actions {
    width: 100%;
    justify-content: flex-start;
    gap: 0.25rem;
  }

  .nav-btn {
    padding: 0.5rem 0.7rem;
    font-size: 0.9rem;
  }
}
</style>
