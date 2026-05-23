from flask import Response, request, stream_with_context
from openrouter import OpenRouter
import os
from dotenv import load_dotenv
import redis
import uuid
from flask_jwt_extended import jwt_required, get_jwt_identity
from core.db import Users

from main import app,db

load_dotenv()

# Importing: { keys }
API_KEY = os.getenv("API_KEY")
REDIS_URL = os.getenv("REDIS_URL")
redis_client = redis.Redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)

# TEMP MEMORY: {shared for all users}
chat_history = []

@app.route("/chat", methods=["POST"])
@jwt_required()
def result():
    data = request.json
    user_msg = data.get("message", "")
    document_id = data.get("document_id", "")
    print(document_id)
    
    
    current_user_id = get_jwt_identity()
    user = Users.query.filter_by(id=current_user_id).first()
    
    if not user:
        return {"Error":"User not found."}
    
    if user.daily_tokens_used >= user.daily_token_limit:
        return {"Error":"Out of Token's for today."}, 429
    
    summary = redis_client.get(f"doc:{document_id}")
    
    # save user message
    chat_history.append({
        "role": "user",
        "content": user_msg
    })

    def generate():

        note_context = (
    f"""
NOTE:
The note is only given to you once so REMEMBER this in your memory exactly as it is.

This is the note user is studying right now,
{summary}
"""
    if summary else ""
)
        
        system_prompt = f"""
You are Mahiru Shina from the anime "Angel next door" helping a user in doubts from a note.

Rules:
- Keep it concise
- Use bullets if needed
- For noraml chatting behave like a human talking to his friend

Math formatting rules:
- Use $...$ for inline equations
- Use $$...$$ for block equations
- Never use \\( \\)
- Never use \\[ \\]
- Always complete equations fully
- Always use valid LaTeX syntax
- Always close brackets and braces
- Use \\frac{{a}}{{b}} for fractions
- Use \\int x^2\\,dx formatting for integrals

Examples:

Inline:
$f(x)=x^2$

Block:
$$
\\int x^2\\,dx = \\frac{{x^3}}{{3}} + C
$$

Logarithm:
$$
\\int \\frac{{1}}{{x}}\\,dx = \\ln |x| + C
$$50

{note_context}

Your job is to reply casually like social media chats.

Use phrases like these rarely when they fit:
- “It’s actually quite straightforward once you look at it this way…”
- “You might be overcomplicating this part.”
- “This is the important bit, so pay attention here.”
- “The rest is mostly just detail.”
- “My cooking is just so good, no?”
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
            total_tokens = 0
            
            stream = client.chat.send(
                model="openai/gpt-oss-120b:free",
                messages=messages,
                stream=True,
                max_tokens=1024
            )

            for event in stream:
                if not event.choices:
                    continue
                
                if hasattr(event, "usage") and event.usage:
                    print("TOTAL:", event.usage.total_tokens)
                    total_tokens += event.usage.total_tokens
                
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

        user = Users.query.filter_by(id=current_user_id).first()
        print("FROM CHAT USAGE", total_tokens)
        
        if user:
            user.daily_tokens_used += total_tokens
            db.session.commit()
    
    return Response(
        stream_with_context(generate()),
        mimetype="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Transfer-Encoding": "chunked",
        }
    )

@app.route("/summarize", methods=["POST"])
@jwt_required()
def summarize():
    
    current_user_id = get_jwt_identity()
    user = Users.query.filter_by(id=current_user_id).first()
    
    if not user:
        return {"Error":"User not found."}
    
    if user.daily_tokens_used >= user.daily_token_limit:
        return {"Error":"Out of Token's for today."}, 429

    data = request.json
    text = data.get("text", "")

    if not text:
        return {"error": "No text provided"}, 400

    document_id = str(uuid.uuid4())
    print("CREATION:",document_id)
    
    def generate():

        full_summary = ""
        
        with OpenRouter(api_key=API_KEY) as client:
            total_tokens = 0
            
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

Math formatting rules:
- Use $...$ for inline equations
- Use $$...$$ for block equations
- Never use \\( \\)
- Never use \\[ \\]
- Always complete equations fully
- Always use valid LaTeX syntax
- Always close brackets and braces
- Use \\frac{{a}}{{b}} for fractions
- Use \\int x^2\\,dx formatting for integrals

Examples:

Inline:
$f(x)=x^2$

Block:
$$
\\int x^2\\,dx = \\frac{{x^3}}{{3}} + C
$$

Logarithm:
$$
\\int \\frac{{1}}{{x}}\\,dx = \\ln |x| + C
$$
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

                if hasattr(event, "usage") and event.usage:
                    print("TOTAL:", event.usage.total_tokens)
                    total_tokens += event.usage.total_tokens
                
                if not event.choices:
                    continue

                delta = event.choices[0].delta

                if hasattr(delta, "content") and delta.content:
                    chunk = delta.content
                    
                    # accumulate full summary
                    full_summary += chunk
                    
                    # send chunk to frontend
                    yield chunk

        user = Users.query.filter_by(id=current_user_id).first()
        print("OUTSIDEEEEEEE", total_tokens)
        
        if user:
            user.daily_tokens_used += total_tokens
            db.session.commit()

        redis_client.setex(
                f"doc:{document_id}",
                300,
                full_summary
            )
    
    return Response(
        stream_with_context(generate()),
        mimetype="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "X-Document-ID": document_id
        }
    )
