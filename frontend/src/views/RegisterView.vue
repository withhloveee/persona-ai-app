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
                    <i class="bi bi-person-plus"></i>
                  </span>
                  <h1 class="h3 fw-bold mb-2">
                    Create account
                  </h1>
                  <p class="text-secondary mb-0">
                    Set up your profile and start learning.
                  </p>
                </div>

                <form @submit.prevent="registerUser">
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
                      placeholder="Choose a username"
                      autocomplete="username"
                      required
                    >
                  </div>

                  <div class="mb-3">
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
                      placeholder="Create a password"
                      autocomplete="new-password"
                      required
                    >
                  </div>

                  <div class="mb-4">
                    <label
                      for="confirmPassword"
                      class="form-label fw-semibold"
                    >
                      Confirm Password
                    </label>
                    <input
                      id="confirmPassword"
                      v-model="confirmPassword"
                      type="password"
                      class="form-control form-control-lg"
                      placeholder="Confirm your password"
                      autocomplete="new-password"
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
                    Register
                  </button>
                </form>

                <div class="text-center mt-4">
                  <p class="text-secondary mb-2">
                    Already have an account?
                  </p>
                  <RouterLink
                    to="/login"
                    class="btn btn-outline-primary w-100"
                  >
                    Login
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
import router from "@/router"
import { ref } from "vue"
import Appheader from "@/components/Appheader.vue"

const username = ref("")
const password = ref("")
const confirmPassword = ref("")

const error = ref("")

async function registerUser() {
    const resp = await fetch("http://127.0.0.1:8000/register",{
        method:"POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username:username.value,
            password:password.value
        })
    })

    const data = await resp.json()

    if(!resp.ok){
        error.value = data.message || "Registration failed"
        return
    }

    router.push("login")
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
