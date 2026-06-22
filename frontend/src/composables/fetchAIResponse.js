import { ref } from "vue"

export async function fetchAIResponse(input,onChunk,documentId=null,character=null) {

    const response = ref("")
    const token = localStorage.getItem("token")
    console.log("YUM", character)

    try {
        const res = await fetch("http://127.0.0.1:8000/chat",{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
            message: input,
            // if nothing is given: null is passed
            document_id: documentId, 
            character: character
        })
    })

    if(res.status === 422){
        onChunk("It was found you are not logged in.")
        return
    }

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
    } catch (error) {
        console.log(error)
    }

    return response
}