<template>
  <div
    class="container vh-100 d-flex flex-column justify-content-center align-items-center text-center"
  >

    <h1 class="display-5 fw-bold mb-3">
      Welcome to Persona Based Learning
    </h1>

    <p class="text-muted mb-4">
      Learn with AI-powered personalized guidance
    </p>

    <div class="d-flex gap-3">

      <RouterLink
        to="/register"
        class="btn btn-primary px-4"
      >
        Register
      </RouterLink>

      <RouterLink
        to="/login"
        class="btn btn-outline-primary px-4"
      >
        Login
      </RouterLink>

    </div>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>
