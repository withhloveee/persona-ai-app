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
                
                <button class="gsi-material-button w-100" type="button" @click="loginWithGoogle">
                  <div class="gsi-material-button-state"></div>
                  <div class="gsi-material-button-content-wrapper">
                    <div class="gsi-material-button-icon">
                      <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" xmlns:xlink="http://www.w3.org/1999/xlink" style="display: block;">
                        <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"></path>
                        <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"></path>
                        <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"></path>
                        <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"></path>
                        <path fill="none" d="M0 0h48v48H0z"></path>
                      </svg>
                    </div>
                    <span class="gsi-material-button-contents">Sign in with Google</span>
                    <span style="display: none;">Sign in with Google</span>
                  </div>
                </button>

                <!-- <button
                  type="button"
                  class="btn btn-primary btn-lg w-100"
                  @click="loginWithGoogle"
                >
                  <i class="bi bi-google me-2"></i>
                  Continue with Google
                </button> -->
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

// make a GET request to backend route: (login)
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
