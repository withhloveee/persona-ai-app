<template>
  <div class="page-wrapper">

    <Appheader :nav-items="navItems" />

    <div class="self-container flex-grow-1 d-flex justify-content-center align-items-center">

      <div class="card shadow-sm register-card">

        <div class="card-body p-4">

          <h3 class="text-center mb-4 fw-bold">
            Create Account
          </h3>

          <form @submit.prevent="registerUser">

            <div class="mb-3">
              <label class="form-label">
                Username
              </label>

              <input
                v-model="username"
                type="text"
                class="form-control"
                placeholder="Choose a username"
                required
              >
            </div>

            <div class="mb-3">
              <label class="form-label">
                Password
              </label>

              <input
                v-model="password"
                type="password"
                class="form-control"
                placeholder="Enter password"
                required
              >
            </div>

            <div class="mb-3">
              <label class="form-label">
                Confirm Password
              </label>

              <input
                v-model="confirmPassword"
                type="password"
                class="form-control"
                placeholder="Confirm password"
                required
              >
            </div>

            <button
              type="submit"
              class="btn btn-primary w-100 mt-2"
            >
              Register
            </button>

          </form>

          <div
            v-if="error"
            class="alert alert-danger mt-3 mb-0 text-center"
          >
            {{ error }}
          </div>

          <p class="text-center mt-4 mb-2">
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

.self-container {
  flex: 1;
  background-color: #f6f8fe;
  background-image: radial-gradient(
    rgba(37, 99, 235, 0.08) 0.6px,
    transparent 3px
  );
  background-size: 30px 30px;
}

.register-card {
  width: 100%;
  max-width: 450px;
  border-radius: 16px;
}
</style>