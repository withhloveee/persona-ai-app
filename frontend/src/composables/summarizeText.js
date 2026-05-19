import { useSummaryStore } from "@/stores/chat"

export async function summarizeText(text) {

    const summaryStore = useSummaryStore()
    summaryStore.summaryReady = false

    // clear old markdown
    summaryStore.markdown = ""

    const res = await fetch("http://localhost:5000/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    })

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
}