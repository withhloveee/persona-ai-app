<template>
  <div class="landing-page-wrapper">
    <Appheader :nav-items="navItems" />

    <section class="hero-section d-flex align-items-center justify-content-center">
      <div class="container">
        <div class="hero-card">

          <div class="hero-content">
            <div class="badge-pill mb-4">
              ✨ AI-Powered Learning Platform
            </div>

            <h1 class="hero-title mb-3">
              Learn smarter,<br>
              <span class="text-accent">with your characters.</span>
            </h1>

            <p class="hero-subtitle mb-5">
              Personalized explanations, smart notes, and adaptive learning paths 
              designed to help students study better.
            </p>

            <div class="cta-group">
              <RouterLink v-if="authStore.isLoggedIn" to="/upload" class="btn-primary-custom">
                Upload PDF <span class="arrow">→</span>
              </RouterLink>
              <RouterLink v-else to="/register" class="btn-primary-custom">
                Start Learning
              </RouterLink>
            </div>

            <p class="cta-sub mt-3">
              Already have an account? 
              <RouterLink to="/login" class="link-underline">Sign in here</RouterLink>
            </p>
          </div>

          <div class="hero-illustration">
            <img src="@/assets/anime-girl.png" alt="Study character" class="character-img" />
          </div>

        </div>
      </div>
    </section>

    <section class="features-section">
      <div class="container py-5">

        <div class="text-center mb-5">
          <p class="section-eyebrow">What's inside</p>
          <h2 class="section-heading">
            Built for smarter learning
          </h2>
        </div>

        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">✨</div>
            <h3 class="feature-title">Personalized guidance</h3>
            <p class="feature-desc">
              Explanations and learning support adapted to your level and pace — not a one-size-fits-all answer.
            </p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">📝</div>
            <h3 class="feature-title">Smart notes</h3>
            <p class="feature-desc">
              Clean summaries and structured notes generated from your PDFs for faster, better revision.
            </p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3 class="feature-title">Easy to use</h3>
            <p class="feature-desc">
              A clean UI that gets out of your way so you can focus on studying, not figuring out the tool.
            </p>
          </div>
        </div>

      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import Appheader from '@/components/Appheader.vue'
import { useAuthStore } from '@/stores/chat';

const authStore = useAuthStore()

const navItems = [
  { label: "Home", icon: "house-door", active: true },
  { label: "About", icon: "info-circle", active: false }
]

const isLoggedIn = ref(!!localStorage.getItem("token"))
</script>

<style scoped>
/* =====================
   LAYOUT
===================== */
.landing-page-wrapper {
  display: grid;
  grid-template-rows: auto 1fr;
  min-height: 100vh;
  /* Bugster-style noise/dot texture background */
  background-color: #e8e5df;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4'%3E%3Crect width='4' height='4' fill='%23e8e5df'/%3E%3Crect x='0' y='0' width='1' height='1' fill='rgba(0,0,0,0.07)'/%3E%3C/svg%3E");
  background-size: 4px 4px;
}

.hero-section {
  min-height: calc(100vh - 58px);
  width: 100%;
  padding: 2rem 0 3rem;
}

/* =====================
   HERO CARD (Bugster's big rounded card)
===================== */
.hero-card {
  background-color: #f5f2ec;
  border: 1.5px solid rgba(0, 0, 0, 0.1);
  border-radius: 24px;
  padding: 3.5rem 3.5rem 3rem;
  display: flex;
  align-items: center;
  gap: 3rem;
  position: relative;
  overflow: hidden;
  max-width: 960px;
  margin: 0 auto;
}

.hero-content {
  flex: 1;
  min-width: 0;
}

/* =====================
   BADGE PILL
===================== */
.badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.03em;
  color: #1a1a1a;
  background: rgba(255, 255, 255, 0.7);
  border: 1.5px solid rgba(0, 0, 0, 0.12);
  border-radius: 999px;
  padding: 5px 14px;
}

/* =====================
   HERO TYPOGRAPHY
===================== */
.hero-title {
  font-family: "Geist Mono", monospace;
  font-size: clamp(2rem, 4.5vw, 3rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.04em;
  color: #111111;
}

.text-accent {
  color: #2563eb;
}

.hero-subtitle {
  font-size: 1rem;
  color: #555;
  line-height: 1.65;
  max-width: 420px;
}

/* =====================
   CTA BUTTONS
===================== */
.cta-group {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-primary-custom {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background-color: #d8f25c;
  color: #111111;
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 0.7rem 1.5rem;
  border-radius: 8px;
  border: 1.5px solid rgba(0, 0, 0, 0.15);
  text-decoration: none;
  transition: background-color 0.2s ease, transform 0.1s ease;
}

.btn-primary-custom:hover {
  background-color: #c8e44a;
}

.btn-primary-custom:active {
  transform: scale(0.98);
}

.arrow {
  font-size: 1rem;
}

.cta-sub {
  font-size: 0.85rem;
  color: #777;
  margin-bottom: 0;
}

.link-underline {
  color: #2563eb;
  text-decoration: underline;
  text-underline-offset: 3px;
}

/* =====================
   ILLUSTRATION PANEL
===================== */
.hero-illustration {
  flex-shrink: 0;
  width: 260px;
  height: 280px;
  position: relative;
}

.illustration-blob {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 60% 60%, rgba(37, 99, 235, 0.15) 0%, rgba(216, 242, 92, 0.15) 100%);
  border-radius: 50%;
  transform: scale(1.1);
}

.character-emoji {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 6rem;
  line-height: 1;
  filter: drop-shadow(0 4px 16px rgba(0,0,0,0.08));
  animation: float 4s ease-in-out infinite;
}

.floating-card {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 10px;
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  padding: 9px 14px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  white-space: nowrap;
  animation: floatCard 5s ease-in-out infinite;
}

.card-1 {
  top: 10px;
  left: -10px;
  animation-delay: 0s;
}

.card-2 {
  top: 120px;
  right: -10px;
  animation-delay: 1.5s;
}

.card-icon {
  font-size: 1.3rem;
}

.card-label {
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #999;
  line-height: 1;
  margin-bottom: 2px;
}

.card-title {
  font-size: 0.8rem;
  font-weight: 600;
  color: #111;
  line-height: 1.2;
}

/* =====================
   ANIMATIONS
===================== */
@keyframes float {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50%       { transform: translateX(-50%) translateY(-10px); }
}

@keyframes floatCard {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-6px); }
}

/* =====================
   FEATURES SECTION
===================== */
.features-section {
  background-color: #ffffff;
  border-top: 1.5px solid rgba(0, 0, 0, 0.07);
}

.section-eyebrow {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #2563eb;
  margin-bottom: 6px;
}

.section-heading {
  font-size: 1.75rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #111;
  font-family: 'Georgia', 'Times New Roman', serif;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
}

.feature-card {
  border: 1.5px solid rgba(0, 0, 0, 0.08);
  border-radius: 16px;
  background-color: #fafafa;
  padding: 1.5rem;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.feature-card:hover {
  transform: translateY(-3px);
  border-color: rgba(37, 99, 235, 0.3);
}

.feature-icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background-color: #f0f4ff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  margin-bottom: 1rem;
}

.feature-title {
  font-size: 1rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 0.5rem;
  letter-spacing: -0.01em;
}

.feature-desc {
  font-size: 0.875rem;
  color: #666;
  line-height: 1.6;
  margin: 0;
}

.hero-card {
  position: relative;
  overflow: hidden;
}

.hero-illustration {
  position: absolute;
  right: 20px;
  bottom: 0;
  width: 340px;
  height: auto;
}

.character-img {
  width: 100%;
  height: auto;
  display: block;
}

/* =====================
   RESPONSIVE
===================== */
@media (max-width: 768px) {
  .hero-card {
    flex-direction: column;
    padding: 2rem 1.5rem;
    gap: 2rem;
  }

  .hero-illustration {
    width: 100%;
    height: 180px;
  }

  .character-emoji {
    font-size: 4rem;
  }

  .card-1 { top: 0; left: 0; }
  .card-2 { top: 60px; right: 0; }
  
}

/* =====================
   SCROLLBAR
===================== */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: rgba(136, 136, 136, 0.2);
  border-radius: 999px;
}
</style>

<style>
/* @import url('https://fonts.googleapis.com/css2?family=Geist+Mono:wght@100..900&display=swap'); */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: rgba(136, 136, 136, 0.15);
  border-radius: 999px;
}
</style>