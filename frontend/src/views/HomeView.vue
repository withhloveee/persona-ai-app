<template>
  <div class="landing-page-wrapper">
    <Appheader :nav-items="navItems" />

    <main>
      <section class="hero-section">
        <div class="container-fluid hero-container">
          <div class="row align-items-center justify-content-center g-4 g-lg-5">
            <div class="col-lg-5 col-xl-6 hero-copy">
              <h1 class="hero-title fw-bold mb-3">
                Learn smarter with your favorite study characters.
              </h1>

              <p class="hero-subtitle text-secondary mb-4">
                Personalized explanations, structured notes, and PDF summaries
                designed to help students study with more clarity.
              </p>

              <div class="d-flex flex-column flex-sm-row gap-3">
                <RouterLink
                  v-if="authStore.isLoggedIn"
                  to="/upload"
                  class="btn btn-primary btn-lg px-4"
                >
                  Upload PDF
                  <i class="bi bi-arrow-right ms-2"></i>
                </RouterLink>

                <RouterLink
                  v-else
                  to="/register"
                  class="btn btn-primary btn-lg px-4"
                >
                  Start Learning
                </RouterLink>

                <RouterLink
                  to="/login"
                  class="btn btn-outline-secondary btn-lg px-4"
                >
                  Sign In
                </RouterLink>
              </div>
            </div>

            <div class="col-lg-4 col-xl-4 hero-art-column">
              <div class="hero-visual">
                <img
                  src="@/assets/anime-girl.png"
                  alt="Study character"
                  class="img-fluid hero-image"
                >
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="bg-white border-top">
        <div class="container py-5">
          <div class="row justify-content-center text-center mb-4">
            <div class="col-lg-7">
              <h2 class="h1 fw-bold mb-3">
                Built for focused learning
              </h2>
              <p class="text-secondary mb-0">
                Simple tools for summarizing notes, understanding concepts, and
                keeping study sessions moving.
              </p>
            </div>
          </div>

          <div class="row g-4">
            <div class="col-md-4">
              <div class="card h-100 border-0 shadow-sm feature-card">
                <div class="card-body p-4">
                  <div class="feature-icon feature-icon-primary mb-3">
                    <i class="bi bi-person-check"></i>
                  </div>
                  <h3 class="h5 fw-bold mb-2">
                    Personalized guidance
                  </h3>
                  <p class="text-secondary mb-0">
                    Explanations and learning support adapted to your level and
                    pace.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-md-4">
              <div class="card h-100 border-0 shadow-sm feature-card">
                <div class="card-body p-4">
                  <div class="feature-icon feature-icon-accent mb-3">
                    <i class="bi bi-journal-text"></i>
                  </div>
                  <h3 class="h5 fw-bold mb-2">
                    Smart notes
                  </h3>
                  <p class="text-secondary mb-0">
                    Clean summaries and structured notes generated from your
                    PDFs for faster revision.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-md-4">
              <div class="card h-100 border-0 shadow-sm feature-card">
                <div class="card-body p-4">
                  <div class="feature-icon feature-icon-neutral mb-3">
                    <i class="bi bi-lightning-charge"></i>
                  </div>
                  <h3 class="h5 fw-bold mb-2">
                    Easy to use
                  </h3>
                  <p class="text-secondary mb-0">
                    A clean interface that lets you focus on studying instead of
                    managing the tool.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import Appheader from '@/components/Appheader.vue'
import { useAuthStore } from '@/stores/chat'

const authStore = useAuthStore()

const navItems = [
  { label: 'Home', icon: 'house-door', active: true },
  { label: 'About', icon: 'info-circle', active: false },
]
</script>

<style scoped>
.landing-page-wrapper {
  min-height: 100vh;
  background: var(--app-surface);
}

.hero-section {
  min-height: clamp(520px, 76svh, 700px);
  display: flex;
  align-items: center;
  background:
    linear-gradient(90deg, #ffffff 0%, var(--app-surface) 58%, rgba(185, 216, 74, 0.12) 100%),
    var(--app-surface);
  overflow: hidden;
}

.hero-container {
  max-width: 1080px;
  padding: clamp(2.25rem, 5vw, 4.5rem) clamp(1rem, 3vw, 2rem);
}

.hero-copy {
  position: relative;
  z-index: 2;
}

.hero-title {
  color: var(--app-ink);
  font-size: clamp(2.15rem, 4.0vw, 3.55rem);
  letter-spacing: -0.02em;
  line-height: 1.04;
  max-width: 15ch;
}

.hero-subtitle {
  max-width: 31rem;
  font-size: clamp(0.98rem, 1.05vw, 1.08rem);
  line-height: 1.58;
}

.hero-section .btn {
  border-radius: 0.75rem;
  font-weight: 700;
}

.hero-art-column {
  display: flex;
  justify-content: center;
}

.hero-visual {
  width: min(100%, 460px);
  background: transparent;
  opacity: 0.88;
}

.hero-image {
  width: 100%;
  max-height: 560px;
  object-fit: contain;
  object-position: bottom center;
}

.feature-card {
  border-radius: 0.75rem;
  border: 1px solid var(--app-border) !important;
  box-shadow: none !important;
}

.feature-icon {
  width: 3rem;
  height: 3rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.75rem;
  font-size: 1.35rem;
}

.feature-icon-primary {
  color: var(--app-primary);
  background: rgba(36, 84, 214, 0.1);
}

.feature-icon-accent {
  color: #5b6f16;
  background: rgba(185, 216, 74, 0.24);
}

.feature-icon-neutral {
  color: var(--app-ink);
  background: #eef1f6;
}

@media (min-width: 992px) {
  .hero-section {
    min-height: calc(82svh - 32px);
  }
}

@media (max-width: 991.98px) {
  .hero-section {
    min-height: auto;
  }

  .hero-container {
    padding: 2.5rem clamp(1rem, 5vw, 3rem);
  }

  .hero-title {
    max-width: 14ch;
  }

  .hero-art-column {
    justify-content: center;
  }

  .hero-visual {
    width: min(100%, 320px);
    transform: none;
  }
}

@media (max-width: 575.98px) {
  .hero-section .btn {
    width: 100%;
  }
}
</style>
