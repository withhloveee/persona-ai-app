<template>
  <div>
    <input type="file" accept=".pdf" id="pdfInput" @change="handlePDF">
  </div>
</template>

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
