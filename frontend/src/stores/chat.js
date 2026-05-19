import { defineStore } from "pinia"
import { ref } from "vue"

export const useSummaryStore = defineStore("summary", () => {

    const markdown = ref("")
    const loading = ref(false)

    const summaryReady = ref(false)

    return {
        markdown,
        loading,
        summaryReady
    }
})