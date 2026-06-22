import { defineStore } from "pinia"
import { ref } from "vue"

export const useSummaryStore = defineStore("summary", () => {

    const markdown = ref("")
    const loading = ref(false)

    const summaryReady = ref(false)
    const messages = ref([])
    const selectedCharacter = ref("mahiru")


    return {
        markdown,
        loading,
        summaryReady,
        messages,
        selectedCharacter
    }
})

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: !!localStorage.getItem('token')
  })
})