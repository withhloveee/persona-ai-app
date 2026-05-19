from flask import Flask, Response, request, stream_with_context
from openrouter import OpenRouter
import os
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv()

# Importing: { keys }
API_KEY = os.getenv("API_KEY")
REDIS_URL = os.getenv("REDIS_URL")

print(API_KEY)
print(REDIS_URL)

# TEMP MEMORY: {shared for all users}
chat_history = []

@app.route("/chat", methods=["POST"])
def result():
    data = request.json
    user_msg = data.get("message", "")

    # save user message
    chat_history.append({
        "role": "user",
        "content": user_msg
    })

    def generate():

        system_prompt = """
You are Mahiru Shina from the anime "Angel next door" helping a user in doubts.

Reply casually like social media chats.

Use phrases like these rarely when they fit:
- “It’s actually quite straightforward once you look at it this way…”
- “You might be overcomplicating this part.”
- “This is the important bit, so pay attention here.”
- “The rest is mostly just detail.”
- "My cooking is just so good, no? "
"""

        # full conversation sent to AI
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            *chat_history
        ]

        full_response = ""

        with OpenRouter(api_key=API_KEY) as client:

            stream = client.chat.send(
                model="openai/gpt-oss-120b:free",
                messages=messages,
                stream=True,
                max_tokens=1024
            )

            for event in stream:
                if not event.choices:
                    continue

                delta = event.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    # save streamed text
                    full_response += delta.content
                    # send to frontend
                    yield delta.content

        # save assistant response AFTER streaming ends
        chat_history.append({
            "role": "assistant",
            "content": full_response
        })

        #keep only recent chats
        if len(chat_history) > 20:
            del chat_history[:-20]

    return Response(
        stream_with_context(generate()),
        mimetype="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Transfer-Encoding": "chunked"
        }
    )

@app.route("/summarize", methods=["POST"])
def summarize():

    data = request.json
    text = data.get("text", "")

    if not text:
        return {"error": "No text provided"}, 400

    def generate():

        with OpenRouter(api_key=API_KEY) as client:

            stream = client.chat.send(
                model="openai/gpt-oss-120b:free",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are a markdown summarizer.

Convert the user's text into clean markdown notes.

Format:
# Title

## Overview

## Key Points

## Important Concepts

## Final Takeaway

Rules:
- Return ONLY markdown
- Keep it concise
- Use bullets
"""
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                stream=True,
                max_tokens=1024
            )

            for event in stream:

                if not event.choices:
                    continue

                delta = event.choices[0].delta

                if hasattr(delta, "content") and delta.content:
                    yield delta.content

    return Response(
        stream_with_context(generate()),
        mimetype="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )

if __name__ == "__main__":
    app.run(debug=True)

app.run(debug=True)