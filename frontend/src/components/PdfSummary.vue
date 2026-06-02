<template>

  <div class="d-flex flex-column ps-4 h-100">

    <!-- HEADER -->
    <div class="border-bottom p-3">
      <h5 class="m-0">Notes created</h5>
    </div>

    <!-- CONTENT -->
    <div
      class="flex-grow-1 p-3 chat-scroll d-flex flex-column"
      style="min-height: 0;"
    >

      <!-- REAL CONTENT -->
      <div
        v-if="markdown"
        class="markdown-body p-4 rounded"
        v-html="parsedMarkdown"
      ></div>

      <!-- SKELETON -->
      <div
        v-else
        class="placeholder-glow w-100 h-100 d-flex flex-column"
      >
        <!-- MAIN TITLE -->
        <div class="mb-4">
          <div
            class="placeholder col-5"
            style="height: 42px;"
          ></div>
        </div>

        <!-- SUBTITLE -->
        <div class="mb-3">
          <div
            class="placeholder col-3"
            style="height: 28px;"
          ></div>
        </div>

        <!-- PARAGRAPH -->
        <div class="mb-5">

          <div
            class="placeholder col-12 mb-2"
            style="height: 18px;"
          ></div>

          <div
            class="placeholder col-12 mb-2"
            style="height: 18px;"
          ></div>

          <div
            class="placeholder col-10 mb-2"
            style="height: 18px;"
          ></div>

          <div
            class="placeholder col-8"
            style="height: 18px;"
          ></div>

        </div>

        <!-- SECOND HEADING -->
        <div class="mb-3">
          <div
            class="placeholder col-4"
            style="height: 30px;"
          ></div>
        </div>

        <!-- SECOND PARAGRAPH -->
        <div class="mb-4">

          <div
            class="placeholder col-12 mb-2"
            style="height: 18px;"
          ></div>

          <div
            class="placeholder col-12 mb-2"
            style="height: 18px;"
          ></div>

          <div
            class="placeholder col-9"
            style="height: 18px;"
          ></div>

        </div>

        <!-- LARGE CONTENT AREA -->
        <div
          class="placeholder col-12 flex-grow-1"
          style="min-height: 300px;"
        ></div>

      </div>

    </div>

  </div>

</template>

<script setup>
import { computed } from "vue"
import { marked } from "marked"
import markedKatex from "marked-katex-extension"
import "katex/dist/katex.min.css"
import DOMPurify from "dompurify"

import { useSummaryStore } from "@/stores/chat"
import { storeToRefs } from "pinia"

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

      return `
        <pre>
          <code class="hljs language-${language}">
            ${highlighted}
          </code>
        </pre>
      `
    }
  }
})

const chatStore = useSummaryStore()
const { markdown } = storeToRefs(chatStore)

// run every time {markdown.value} changes
const parsedMarkdown = computed(() => {
    let rawHTML =  marked.parse(markdown.value)
    let cleanHTML = DOMPurify.sanitize(rawHTML)
    return cleanHTML
})

console.log(marked.parse(markdown.value))
</script>

