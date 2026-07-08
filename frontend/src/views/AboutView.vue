<template>
  <div class="about-page-wrapper">
    <Appheader :nav-items="navItems" />

    <main class="about-main">
      <section class="about-intro" aria-labelledby="about-title">
        <div class="about-container">
          <p class="about-kicker">
            About Talk2learn
          </p>
          <div class="about-intro-grid">
            <div>
              <h1 id="about-title" class="about-title">
                A focused study tool built by one independent developer.
              </h1>
              <p class="about-lead">
                Talk2learn helps students turn study material into clearer summaries,
                structured notes, and conversational explanations. It exists to make
                learning feel less scattered and more approachable.
              </p>
            </div>

            <aside class="maker-note" aria-label="Project maintenance note">
              <span class="maker-note-label">Maintained independently</span>
              <p>
                This is a side project, developed and improved alongside other
                responsibilities. Every improvement is made with the goal of keeping
                the app useful, clear, and dependable for the people who rely on it.
              </p>
            </aside>
          </div>
        </div>
      </section>

      <section class="about-content" aria-label="About details">
        <div class="about-container">
          <div class="content-grid">
            <article class="about-section">
              <span class="section-icon" aria-hidden="true">
                <i class="bi bi-journal-text"></i>
              </span>
              <div>
                <h2>About the project</h2>
                <p>
                  Talk2learn is designed for students who want faster ways to
                  understand notes, review documents, and keep study sessions moving.
                  The application focuses on practical learning support rather than
                  replacing the effort of studying.
                </p>
              </div>
            </article>

            <article class="about-section">
              <span class="section-icon" aria-hidden="true">
                <i class="bi bi-person-workspace"></i>
              </span>
              <div>
                <h2>About the developer</h2>
                <p>
                  The project is designed, developed, maintained, and improved by a
                  single independent developer. That means progress is personal,
                  deliberate, and shaped by real feedback from people using the app.
                </p>
              </div>
            </article>

            <article class="about-section">
              <span class="section-icon" aria-hidden="true">
                <i class="bi bi-compass"></i>
              </span>
              <div>
                <h2>Why this project exists</h2>
                <p>
                  Talk2learn was created from a simple motivation: learning tools
                  should reduce friction. The goal is to help users spend less time
                  organizing material and more time understanding it.
                </p>
              </div>
            </article>

            <article class="about-section support-section">
              <span class="section-icon" aria-hidden="true">
                <i class="bi bi-heart"></i>
              </span>
              <div>
                <h2>Support the project</h2>
                <p>
                  If Talk2learn is useful to you, support is welcome and appreciated.
                  Donations or other forms of support can help keep development moving,
                  but they are never expected or required.
                </p>
                <div class="support-placeholder" aria-label="Support links placeholder">
                  Support links can be added here later.
                </div>
              </div>
            </article>

            <article class="about-section">
              <span class="section-icon" aria-hidden="true">
                <i class="bi bi-arrow-repeat"></i>
              </span>
              <div>
                <h2>Future improvements</h2>
                <p>
                  The app will continue to improve over time with better summaries,
                  smoother study workflows, and refinements based on what users need
                  most. Development is ongoing, steady, and intentionally practical.
                </p>
              </div>
            </article>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import Appheader from '@/components/Appheader.vue'

const router = useRouter()

const navItems = [
  {
    label: 'Home',
    icon: 'house-door',
    action: () => router.push('/'),
  },
  {
    label: 'About',
    icon: 'info-circle',
    active: true,
    action: () => router.push('/about'),
  },
]
</script>

<style scoped>
.about-page-wrapper {
  min-height: 100vh;
  background: var(--app-surface);
}

.about-main {
  color: var(--app-ink);
}

.about-container {
  width: min(100% - 2rem, 1060px);
  margin: 0 auto;
}

.about-intro {
  background:
    linear-gradient(180deg, #ffffff 0%, rgba(247, 248, 251, 0.96) 100%);
  border-bottom: 1px solid var(--app-border);
  padding: clamp(3rem, 7vw, 5.5rem) 0 clamp(2.25rem, 5vw, 4rem);
}

.about-kicker {
  color: var(--app-primary);
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  margin-bottom: 0.9rem;
  text-transform: uppercase;
}

.about-intro-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 360px);
  gap: clamp(1.5rem, 5vw, 4rem);
  align-items: start;
}

.about-title {
  max-width: 780px;
  margin: 0;
  color: var(--app-ink);
  font-size: clamp(2rem, 4vw, 3.45rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.08;
}

.about-lead {
  max-width: 680px;
  margin: 1.25rem 0 0;
  color: var(--app-muted);
  font-size: clamp(1rem, 1.2vw, 1.12rem);
  line-height: 1.7;
}

.maker-note {
  border: 1px solid var(--app-border);
  border-left: 5px solid var(--app-accent);
  border-radius: 0.5rem;
  background: #ffffff;
  padding: 1.35rem;
  box-shadow: 0 18px 50px rgba(20, 33, 61, 0.07);
}

.maker-note-label {
  display: inline-flex;
  margin-bottom: 0.85rem;
  color: var(--app-primary-dark);
  font-family: "Geist Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.maker-note p {
  margin: 0;
  color: var(--app-muted);
  font-size: 0.96rem;
  line-height: 1.7;
}

.about-content {
  padding: clamp(2.5rem, 6vw, 4.75rem) 0;
}

.content-grid {
  display: grid;
  gap: 1rem;
}

.about-section {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 1rem;
  align-items: start;
  border: 1px solid var(--app-border);
  border-radius: 0.75rem;
  background: #ffffff;
  padding: clamp(1.25rem, 3vw, 1.8rem);
}

.section-icon {
  width: 2.75rem;
  height: 2.75rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.75rem;
  background: rgba(36, 84, 214, 0.1);
  color: var(--app-primary);
  font-size: 1.2rem;
}

.about-section h2 {
  margin: 0 0 0.55rem;
  color: var(--app-ink);
  font-size: clamp(1.15rem, 2vw, 1.4rem);
  font-weight: 800;
  line-height: 1.2;
}

.about-section p {
  max-width: 760px;
  margin: 0;
  color: var(--app-muted);
  line-height: 1.72;
}

.support-section {
  background:
    linear-gradient(90deg, rgba(36, 84, 214, 0.05), rgba(185, 216, 74, 0.12)),
    #ffffff;
}

.support-section .section-icon {
  background: rgba(185, 216, 74, 0.25);
  color: #5b6f16;
}

.support-placeholder {
  width: fit-content;
  max-width: 100%;
  margin-top: 1rem;
  border: 1px dashed rgba(36, 84, 214, 0.42);
  border-radius: 0.5rem;
  background: rgba(255, 255, 255, 0.72);
  color: var(--app-primary-dark);
  font-size: 0.92rem;
  font-weight: 700;
  padding: 0.75rem 0.9rem;
}

@media (max-width: 767.98px) {
  .about-intro-grid,
  .about-section {
    grid-template-columns: 1fr;
  }

  .about-container {
    width: min(100% - 1.25rem, 1060px);
  }

  .maker-note,
  .about-section {
    border-radius: 0.65rem;
  }
}
</style>
