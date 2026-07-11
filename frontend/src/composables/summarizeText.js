import { useSummaryStore } from "@/stores/chat"

export async function summarizeText(text) {

    const summaryStore = useSummaryStore()
    summaryStore.summaryReady = false
    const token = localStorage.getItem("token")

    // reset the chat to Nothing
    summaryStore.messages = []
    // clear old markdown
    summaryStore.markdown = ""

    try {
        const res = await fetch("http://127.0.0.1:8000/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
            text: text
        })
    })

    if(res.status === 422){
        summaryStore.markdown += "It was found you are not logged in."
        return
    }

    // store the id to { session-storage }
    const documentId = res.headers.get("X-Document-ID")
    console.log("WHAT I GOT IS ", documentId)
    sessionStorage.setItem("document_id", documentId)

    const reader = res.body.getReader()
    const decoder = new TextDecoder()

    while (true) {

        const { done, value } = await reader.read()

        if (done) {
            summaryStore.summaryReady = true
            break
        }

        const chunk = decoder.decode(value)

        // THIS triggers live rendering
        summaryStore.markdown += chunk
    }
    } catch (error) {
        console.log("From catch:", error)
    }

}
