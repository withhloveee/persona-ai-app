import { ref } from "vue"

export async function fetchAIResponse(input,onChunk) {
    const response = ref("")

    const res = await fetch("http://localhost:5000/chat",{
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },
        
        body: JSON.stringify({
            message: input
        })
    })

    const reader = res.body.getReader()
    const decoder = new TextDecoder()

    while (true) {
        const result = await reader.read()

        // Stream finished
        if (result.done) {
            break
        }
        const text = decoder.decode(result.value)

        onChunk(text)
    }

    return response
}