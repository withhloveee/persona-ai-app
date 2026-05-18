import { defineStore } from "pinia"
import { ref } from "vue"

export const useSummaryStore = defineStore("summary", () => {

    const markdown = ref("")
    const loading = ref(false)

    return {
        markdown,
        loading
    }
})