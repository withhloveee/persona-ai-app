<template>
  <Splitpanes class="default-theme vh-100">

    <Pane size="50">
      <PdfSummary />
    </Pane>

    <Pane size="50">
      <ChatBot />
    </Pane>

  </Splitpanes>
</template>

<script setup>
import ChatBot from '@/components/ChatBot.vue';
import PdfSummary from '@/components/PdfSummary.vue';
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
</script>