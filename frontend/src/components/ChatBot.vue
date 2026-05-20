<template>

  <div class="d-flex flex-column h-100">

    <!-- HEADER -->
    <div class="border-bottom p-3">
      <h5 class="m-0">AI Chat</h5>
    </div>

    <!-- MESSAGES -->
    <div
      class="flex-grow-1 p-3 chat-scroll"
      style="min-height: 0;"
    >

      <div
        v-for="(message, index) in messages"
        :key="index"
        class="mb-3"
      >

        <!-- USER -->
        <div
          v-if="message.role === 'user'"
          class="d-flex justify-content-end"
        >
          <div class="bg-primary text-white p-2 rounded">
            {{ message.content }}
          </div>
        </div>

        <!-- AI -->
        <div
          v-else
          class="d-flex justify-content-start"
        >
          <div
            class="bg-light p-2 rounded border markdown-body"
            v-html="message.rendered || marked(message.content)"
          ></div>
        </div>

      </div>

    </div>

    <!-- INPUT -->
    <div class="border-top p-3">

      <div class="input-group">

        <input
          v-model="userInput"
          @keydown.enter="sendMessage"
          type="text"
          class="form-control"
          placeholder="Ask something..."
        >

        <button
          @click="sendMessage"
          class="btn btn-primary"
        >
          Send
        </button>

      </div>

    </div>

  </div>

</template>

<script setup>
import { ref,watch  } from 'vue'
import { marked } from "marked"
import { useSummaryStore } from '@/stores/chat'

import { fetchAIResponse } from '@/composables/fetchAIResponse'
import markedKatex from "marked-katex-extension"
import "katex/dist/katex.min.css"

marked.use(markedKatex())
const summaryStore = useSummaryStore()

const userInput = ref('')
const messages = ref([])

async function sendMessage() {

  if (!userInput.value.trim()) return

  messages.value.push({
    role: 'user',
    content: userInput.value
  })

  const question = userInput.value

  userInput.value = ''

  // plain object
  const aiMessage = ref({
    role: 'assistant',
    content: '',
    rendered: ''
})

  messages.value.push(aiMessage.value)

  // streaming updates
  await fetchAIResponse(question, (chunk) => {
    aiMessage.value.content += chunk
  })

  aiMessage.value.rendered = marked(aiMessage.value.content)
}

watch(
  () => summaryStore.summaryReady,
  async (ready) => {

    if (!ready) return

    const documentId = sessionStorage.getItem("document_id")
    const aiMessage = ref({
      role: 'assistant',
      content: ''
    })

    messages.value.push(aiMessage.value)

    await fetchAIResponse(
      "Say hello and ask user for doubts about the notes.",
      (chunk) => {
        aiMessage.value.content += chunk
      },
      documentId
    )
    
  }
)


</script>   