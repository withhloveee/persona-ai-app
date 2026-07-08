<template>
  <div>
    <Appheader :nav-items="navItems"></Appheader>

    <div class="self-container d-flex justify-content-center align-items-center">
    <div class="setup-card shadow-sm">

      <!-- Heading -->
      <div class="text-center mb-4">
        <h2 class="fw-bold mb-2">Start Learning</h2>
        <p class="text-muted mb-0">
          Choose your study companion and upload your PDF
        </p>
      </div>

      <!-- Character Selection -->
      <div class="mb-4">
        <h6 class="section-title">Study Companion</h6>

        <div class="character-grid">

          <label
            class="character-card-option"
            :class="{ active: selectedCharacter === 'mahiru' }"
          >
            <input
              type="radio"
              value="mahiru"
              v-model="selectedCharacter"
            >
            <div class="character-emoji"><img src="@/assets/mahiru.jpg" alt="" width="120px"></div>
            <div class="character-name">Mahiru</div>
          </label>

          <label
            class="character-card-option"
            :class="{ active: selectedCharacter === 'fern' }"
          >
            <input
              type="radio"
              value="fern"
              v-model="selectedCharacter"
            >
            <div class="character-emoji"><img src="@/assets/fern.jpg" alt="" width="120px"></div>
            <div class="character-name">Fern</div>
          </label>

          <label
            class="character-card-option"
            :class="{ active: selectedCharacter === 'hayasaka' }"
          >
            <input
              type="radio"
              value="hayasaka"
              v-model="selectedCharacter"
            >
            <div class="character-emoji"><img src="@/assets/hayasaka.jpg" alt="" width="120px"></div>
            <div class="character-name">Hayasaka</div>
          </label>

        </div>
      </div>

      <!-- Upload Box -->
      <label
        for="pdfInput"
        class="upload-box"
      >
        <div class="upload-icon">
          📄
        </div>

        <h5 class="fw-semibold mb-1">
          Upload PDF Notes
        </h5>

        <p class="text-muted mb-0">
          Click to browse and generate a summary
        </p>
      </label>

      <input
        id="pdfInput"
        type="file"
        accept=".pdf"
        class="d-none"
        @change="handlePDF"
      >

    </div>

  </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import { extractPDFText } from '@/composables/extractPDFText'
import { summarizeText } from '@/composables/summarizeText'
import { useSummaryStore } from '@/stores/chat'
import Appheader from '@/components/Appheader.vue'

const router = useRouter()
const chatStore = useSummaryStore()
const { selectedCharacter } = storeToRefs(chatStore)

async function handlePDF(event) {
  const file = event.target.files[0]

  if (!file) return

  router.push('/summarize')

  console.log('Character:', selectedCharacter.value)
  console.log(file.name)

  const text = await extractPDFText(file)
  await summarizeText(text)

  console.log(chatStore.markdown)
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
.self-container {
  min-height: 100vh;
  padding: 2rem;
  background: #f8fafc;
}

.setup-card {
  width: 100%;
  max-width: 720px;
  background: white;
  border-radius: 24px;
  padding: 2rem;
}

.section-title {
  font-weight: 600;
  margin-bottom: 1rem;
}

.character-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.character-card-option {
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  padding: 1rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.character-card-option:hover {
  border-color: #3b82f6;
  transform: translateY(-2px);
}

.character-card-option.active {
  border-color: #2563eb;
  background: #eff6ff;
}

.character-card-option input {
  display: none;
}

.character-emoji {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.character-name {
  font-weight: 600;
}

.upload-box {
  width: 100%;
  min-height: 220px;

  border: 2px dashed #cbd5e1;
  border-radius: 18px;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.upload-box:hover {
  border-color: #2563eb;
  background: #f8fbff;
}

.upload-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

@media (max-width: 768px) {
  .character-grid {
    grid-template-columns: 1fr;
  }

  .setup-card {
    padding: 1.5rem;
  }
}
</style>
