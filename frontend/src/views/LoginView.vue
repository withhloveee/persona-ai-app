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
                    <i class="bi bi-google"></i>
                  </span>

                  <h1 class="h3 fw-bold mb-2">
                    Continue with Google
                  </h1>

                  <p class="text-secondary mb-0">
                    Sign in or create an account with your Google account to
                    start learning.
                  </p>
                </div>

                <button
                  type="button"
                  class="btn btn-primary btn-lg w-100"
                  @click="loginWithGoogle"
                >
                  <i class="bi bi-google me-2"></i>
                  Continue with Google
                </button>
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
import Appheader from "@/components/Appheader.vue"

function loginWithGoogle() {
  window.location.href = "http://localhost:8000/login/google"
}

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
