<template>
  <div>
    <Appheader :nav-items="navItems" :sticky="false"/>
    <Splitpanes 
    class="default-theme content-area" 
    style="height: calc(100vh - 65px)"
    :nav-items="navItems"
    >

    <Pane size="70">
      <PdfSummary />
    </Pane>

    <Pane size="30">
      <ChatBot />
    </Pane>

  </Splitpanes>
  </div>
</template>

<script setup>
import ChatBot from '@/components/ChatBot.vue';
import PdfSummary from '@/components/PdfSummary.vue';
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
import Appheader from '@/components/Appheader.vue';
import { useRouter } from 'vue-router'


const router = useRouter()

// for navbar:
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
  }
]
</script>

