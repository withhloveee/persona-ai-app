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
            v-if="message.loading"
            class="typing-loader"
          >
            <span></span>
            <span></span>
            <span></span>
          </div>

          <!-- REAL MESSAGE -->
          <div
            v-else
            class="markdown-body rounded"
            v-html="message.rendered"
            style="padding: 12px;"
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
import { storeToRefs } from "pinia"

import { fetchAIResponse } from '@/composables/fetchAIResponse'
import markedKatex from "marked-katex-extension"
import "katex/dist/katex.min.css"
import DOMPurify from "dompurify"

// code highlight imports
import { markedHighlight } from "marked-highlight"
import hljs from "highlight.js"
import "highlight.js/styles/github.css"

marked.use(markedKatex())
marked.use({
  renderer: {
    code({ text, lang }) {

      const language =
        hljs.getLanguage(lang) ? lang : 'plaintext'

      const highlighted = hljs.highlight(text, {
        language
      }).value

      return `<pre><code class="hljs language-${language}">${highlighted}</code></pre>`
    }
  }
})

const summaryStore = useSummaryStore()
const { messages } = storeToRefs(summaryStore)
const { selectedCharacter } = storeToRefs(summaryStore) 

const userInput = ref('')

function createAIMessage() {
  return ref({
    role: 'assistant',
    content: '',
    rendered: '',
    loading: true
  })
}

async function sendMessage() {
  const documentId = sessionStorage.getItem("document_id")
  console.log("SEND MESSAGE CALLED")
  if (!userInput.value.trim()) return

  messages.value.push({
    role: 'user',
    content: userInput.value
  })

  const question = userInput.value

  userInput.value = ''

  // plain object
  const aiMessage = createAIMessage()

  messages.value.push(aiMessage.value)


  console.log("Inside sendMessage:",documentId)
  
  // streaming updates
  await fetchAIResponse(question, (chunk) => {
    // loading state ends
    aiMessage.value.loading = false

    aiMessage.value.content += chunk
    let rawHTML =  marked.parse(aiMessage.value.content)
    let cleanHTML = DOMPurify.sanitize(rawHTML)

    aiMessage.value.rendered = cleanHTML
  },documentId)

}

watch(
  () => summaryStore.summaryReady,
  async (ready) => {

    if (!ready) return

    const documentId = sessionStorage.getItem("document_id")
    const aiMessage = createAIMessage()

    messages.value.push(aiMessage.value)

    await fetchAIResponse(
      "Say hello and ask user for doubts about the notes.",
      (chunk) => {
        // loading state ends
        aiMessage.value.loading = false

        aiMessage.value.content += chunk
        let rawHTML =  marked.parse(aiMessage.value.content)
        let cleanHTML = DOMPurify.sanitize(rawHTML)

        aiMessage.value.rendered = cleanHTML
      },
      documentId,
      selectedCharacter.value
    )
    
  }
)

</script>

<style scoped>
/* Styles for the loading effect (AI made) */
.typing-loader {
  display: flex;
  gap: 6px;
  padding: 12px;
}

.typing-loader span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #6c757d;

  animation: wave 1.2s infinite ease-in-out;
}

.typing-loader span:nth-child(2) {
  animation-delay: 0.15s;
}

.typing-loader span:nth-child(3) {
  animation-delay: 0.3s;
}

@keyframes wave {
  0%, 60%, 100% {
    transform: translateY(0);
    opacity: 0.5;
  }

  30% {
    transform: translateY(-8px);
    opacity: 1;
  }
}
</style>