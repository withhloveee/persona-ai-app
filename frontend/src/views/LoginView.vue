<template>
  <div class="page-wrapper">

    <Appheader :nav-items="navItems"/>

    <div class="self-container flex-grow-1 d-flex justify-content-center align-items-center">

      <div class="card shadow-sm login-card">

        <div class="card-body p-4">

          <h3 class="text-center mb-4 fw-bold">
            User Login
          </h3>

          <form @submit.prevent="loginUser">

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

            <button
              type="submit"
              class="btn btn-primary w-100 mt-2"
            >
              Login
            </button>

          </form>

          <div
            v-if="error"
            class="alert alert-danger mt-3 mb-0 text-center"
          >
            {{ error }}
          </div>

          <p class="text-center mt-4 mb-2">
            Don't have an account yet?
          </p>

          <RouterLink
            to="/register"
            class="btn btn-outline-primary w-100"
          >
            Register
          </RouterLink>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { ref } from "vue"
import router from "@/router"

import Appheader from "@/components/Appheader.vue"

const username = ref("")
const password = ref("")
const error = ref("")

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

    console.log("Logged in!")
    router.push("upload")

}

// for navbar:
const navItems = [
  {
    label: "Home",
    active: false,
    action: () => router.push("/")
  },
  {
    label: "About",
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

.login-card {
  width: 100%;
  max-width: 425px;
  border-radius: 16px;
}
</style>
