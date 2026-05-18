<template>

  <div class="d-flex flex-column h-100">

    <!-- HEADER -->
    <div class="border-bottom p-3">
      <h5 class="m-0">Notes created</h5>
    </div>

    <!-- CONTENT -->
    <div
    class="flex-grow-1 p-3 chat-scroll"
    style="min-height: 0;"
    >
      <div
        v-if="markdown"
        v-html="parsedMarkdown"
      ></div>

      <p v-else>Please wait for data to arrive.</p>
    </div>

  </div>

</template>

<script setup>
import { computed } from "vue"
import { marked } from "marked"

import { useSummaryStore } from "@/stores/chat"
import { storeToRefs } from "pinia"

const chatStore = useSummaryStore()

const { markdown } = storeToRefs(chatStore)

const parsedMarkdown = computed(() => {
    return marked(markdown.value)
})
</script>