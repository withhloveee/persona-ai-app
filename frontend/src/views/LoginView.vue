<template>
  <div class="page-wrapper">
    <Appheader :nav-items="navItems" />

    <main class="auth-section flex-grow-1 d-flex align-items-center">
      <div class="container py-5">
        <div class="row justify-content-center">
          <div class="col-sm-10 col-md-7 col-lg-5 col-xl-4">
            <div class="card auth-card border-0 shadow-sm">
              <div class="card-body p-4 p-md-5">
                <div class="text-center mb-4">
                  <span class="auth-icon bg-primary-subtle text-primary mb-3">
                    <i class="bi bi-box-arrow-in-right"></i>
                  </span>
                  <h1 class="h3 fw-bold mb-2">
                    Welcome back
                  </h1>
                  <p class="text-secondary mb-0">
                    Sign in to continue learning.
                  </p>
                </div>

                <form @submit.prevent="loginUser">
                  <div class="mb-3">
                    <label
                      for="username"
                      class="form-label fw-semibold"
                    >
                      Username
                    </label>
                    <input
                      id="username"
                      v-model="username"
                      type="text"
                      class="form-control form-control-lg"
                      placeholder="Enter your username"
                      autocomplete="username"
                      required
                    >
                  </div>

                  <div class="mb-4">
                    <label
                      for="password"
                      class="form-label fw-semibold"
                    >
                      Password
                    </label>
                    <input
                      id="password"
                      v-model="password"
                      type="password"
                      class="form-control form-control-lg"
                      placeholder="Enter your password"
                      autocomplete="current-password"
                      required
                    >
                  </div>

                  <div
                    v-if="error"
                    class="alert alert-danger mb-4"
                    role="alert"
                  >
                    {{ error }}
                  </div>

                  <button
                    type="submit"
                    class="btn btn-primary btn-lg w-100"
                  >
                    Login
                  </button>
                </form>

                <div class="text-center mt-4">
                  <p class="text-secondary mb-2">
                    Don't have an account yet?
                  </p>
                  <RouterLink
                    to="/register"
                    class="btn btn-outline-primary w-100"
                  >
                    Create Account
                  </RouterLink>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue"
import router from "@/router"
import { useAuthStore } from "@/stores/chat"

import Appheader from "@/components/Appheader.vue"

const username = ref("")
const password = ref("")
const error = ref("")

const authStore = useAuthStore()

async function loginUser() {
    error.value = ""

    const response = await fetch("http://localhost:8000/login",{
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          username: username.value,
          password: password.value
        })
      }
    )

    const data = await response.json()

    if (!response.ok) {
      error.value = data.message || "Login failed"
      return
    }

    localStorage.setItem(
      "token",
      data.token
    )
    authStore.isLoggedIn = true

    console.log("Logged in!")
    router.push("upload")

}

// for navbar:
const navItems = [
  {
    label: "Home",
    icon: "house-door",
    action: () => router.push("/")
  },
  {
    label: "About",
    icon: "info-circle",
    active: false,
    action: () => router.push("/about")
  }
]
</script>

<style scoped>
.page-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.auth-section {
  background:
    linear-gradient(135deg, rgba(36, 84, 214, 0.08), rgba(185, 216, 74, 0.12)),
    var(--app-surface);
}

.auth-card {
  border-radius: 1rem;
}

.auth-icon {
  width: 3rem;
  height: 3rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.75rem;
  font-size: 1.35rem;
}

.form-control {
  border-color: var(--app-border);
}

.form-control:focus {
  border-color: var(--app-primary);
  box-shadow: 0 0 0 0.25rem rgba(36, 84, 214, 0.14);
}
</style>
