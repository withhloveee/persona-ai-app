<template>
  <div class="d-flex justify-content-center align-items-center vh-100">

    <label
      for="pdfInput"
      class="border border-secondary-subtle rounded-4 px-5 py-5 bg-light
             d-flex flex-column align-items-center
             shadow-sm upload-box"
    >
      <span class="fs-1 mb-3">📄</span>

      <span class="fs-4 fw-semibold">
        Upload PDF
      </span>

      <span class="text-muted mt-1">
        Click to select a file
      </span>
    </label>

    <input
      id="pdfInput"
      type="file"
      accept=".pdf"
      class="d-none"
      @change="handlePDF"
    >

  </div>
</template>

<style scoped>
.upload-box {
  min-width: 320px;
  min-height: 220px;
  cursor: pointer;
  transition: 0.2s ease;
}

.upload-box:hover {
  transform: scale(1.02);
}
</style>

<script setup>
import { useRouter } from 'vue-router'
import { extractPDFText } from '@/composables/extractPDFText'
import { summarizeText } from '@/composables/summarizeText' 
import { useSummaryStore } from "@/stores/chat"


const router = useRouter()
const chatStore = useSummaryStore()

async function handlePDF(event) {
    // Get first selected file
    const file = event.target.files[0]

    // route change
    router.push("summarize");

    console.log(file.name)
    console.log(file.size)
    const text = await extractPDFText(file);
    console.log(text)
    const summary = await summarizeText(text)
    console.log(chatStore.markdown)
    

}
</script>
