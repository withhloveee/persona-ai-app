<template>
  <div class="landing-page-wrapper">
    <Appheader :nav-items="navItems" />

    <section class="hero-section d-flex align-items-center justify-content-center">
      <div class="container text-center">
        <div class="row justify-content-center">
          <div class="col-lg-9 col-xl-8">

            <div class="d-inline-flex align-items-center gap-2 badge-custom mb-4 px-3 py-1.5 rounded-pill border">
              <span class="icon-sparkle text-primary">✨</span>
              <span class="badge-text text-muted small fw-medium">AI-Powered Learning Platform</span>
            </div>

            <h1 class="hero-title fw-bold text-dark mb-3 tracking-tight">
              Learn with guidance <span class="text-primary"> From Your Characters</span>
            </h1>

            <p class="hero-subtitle text-muted mx-auto mb-4 px-md-5">
              Personalized explanations, smart notes, and adaptive learning paths 
              designed to help students study better.
            </p>

            <div class="d-flex gap-3 justify-content-center align-items-center flex-wrap mt-4">
              
              <RouterLink to="/register" class="btn btn-primary px-4 py-2-5 fw-semibold d-inline-flex align-items-center gap-2 shadow-sm">
                Get Started <span>→</span>
              </RouterLink>

              <RouterLink to="/login" class="btn btn-outline-custom px-4 py-2-5 fw-medium d-inline-flex align-items-center gap-2">
                Login to Account
              </RouterLink>

            </div>

          </div>
        </div>
      </div>
    </section>

    <section class="features-section py-5 bg-white">
      <div class="container py-md-5">
        
        <div class="text-center mb-5">
          <h2 class="features-heading fw-bold text-dark mb-2">
            Built for smarter learning
          </h2>
          <p class="text-muted mx-auto" style="max-width: 500px;">
            Everything designed to make studying simpler and more personalized.
          </p>
        </div>

        <div class="row g-4">
          <div class="col-md-4">
            <div class="card feature-card h-100 border p-3">
              <div class="card-body p-2">
                <div class="feature-icon mb-3">
                  <span>✨</span>
                </div>
                <h3 class="h5 fw-bold text-dark mb-2">
                  Personalized Guidance
                </h3>
                <p class="card-text text-muted small mb-0">
                  Get explanations and learning support adapted to your level and pace.
                </p>
              </div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="card feature-card h-100 border p-3">
              <div class="card-body p-2">
                <div class="feature-icon mb-3">
                  <span>📝</span>
                </div>
                <h3 class="h5 fw-bold text-dark mb-2">
                  Smart Notes
                </h3>
                <p class="card-text text-muted small mb-0">
                  Generate clean summaries and structured notes for faster revision.
                </p>
              </div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="card feature-card h-100 border p-3">
              <div class="card-body p-2">
                <div class="feature-icon mb-3">
                  <span>📈</span>
                </div>
                <h3 class="h5 fw-bold text-dark mb-2">
                  Easy To Use
                </h3>
                <p class="card-text text-muted small mb-0">
                  Built with a clean UI/UX to get your work done smoothly and efficiently.
                </p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import Appheader from '@/components/Appheader.vue'

const navItems = [
  {
    label: "Home",
    active: true,
  },
  {
    label: "About",
    active: false,
  }
]
</script>

<style scoped>
/* GENERAL LAYOUT (Uses CSS Grid to dynamic-fit the header safely) */
.landing-page-wrapper {
  display: grid;
  grid-template-rows: auto 1fr;
  min-height: 100vh;
  background-color: #ffffff;
  background-image: radial-gradient(rgba(13, 110, 253, 0.05) 1px, transparent 0);
  background-size: 24px 24px;
}

/* HERO WILL SPAN EXACTLY FROM HEADER BOTTOM TO WINDOW BOTTOM */
.hero-section {
  min-height: calc(100vh - 58px);
  width: 100%;
}

/* SCREENSHOT LAYOUT TYPOGRAPHY & SPACING */
.tracking-tight {
  letter-spacing: -0.03em;
}

.hero-title {
  font-size: calc(2rem + 1.8vw);
  line-height: 1.15;
}

.hero-subtitle {
  font-size: 1.1rem;
  max-width: 640px;
  line-height: 1.6;
}

/* PILL BADGE */
.badge-custom {
  background-color: rgba(255, 255, 255, 0.7);
  border-color: rgba(0, 0, 0, 0.08) !important;
}
.badge-text {
  font-size: 0.8rem;
  letter-spacing: 0.01em;
}

/* BUTTONS */
.btn {
  border-radius: 8px;
  font-size: 0.95rem;
  transition: all 0.2s ease;
}
.py-2-5 {
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
}

.btn-outline-custom {
  background-color: transparent;
  border: 1px solid rgba(0, 0, 0, 0.15);
  color: #475569;
}
.btn-outline-custom:hover {
  background-color: rgba(0, 0, 0, 0.03);
  border-color: rgba(0, 0, 0, 0.25);
  color: #1e293b;
}

/* FEATURES SECTION */

.features-section{
  background-color: #f9f9f9 !important;
}

.features-heading {
  font-size: 1.75rem;
  letter-spacing: -0.02em;
}

.feature-card {
  border-radius: 12px;
  background-color: #ffffff;
  border-color: #e2e8f0 !important;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.feature-card:hover {
  border-color: #cbd5e1 !important;
  transform: translateY(-2px);
}

.feature-icon {
  width: 42px;
  height: 42px;
  border-radius: 8px;
  background-color: rgba(13, 110, 253, 0.08);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
}


/* scroll-styles */
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(136, 136, 136, 0.15);
  border-radius: 999px;
}
</style>

<style>
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(136, 136, 136, 0.15);
  border-radius: 999px;
}
</style>