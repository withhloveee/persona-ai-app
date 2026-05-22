<template>
  <div class="container vh-100 d-flex justify-content-center align-items-center">

    <div class="card shadow-sm login-card" style="width: 27rem;">

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
          Dont have an account yet?
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
</template>

<script setup>
import { ref } from "vue"
import router from "@/router"

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
</script>

<style scoped>
.login-card {
  width: 100%;
  max-width: 425px;
  border-radius: 16px;
}
</style>