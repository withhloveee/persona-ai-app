from flask import Response, request, stream_with_context
from openrouter import OpenRouter
import os
from dotenv import load_dotenv
import redis
import uuid
from flask_jwt_extended import jwt_required, get_jwt_identity
from core.db import Users
import json
from openrouter.errors import TooManyRequestsResponseError

from main import app,db

load_dotenv()

# Importing: { keys }
API_KEY = os.getenv("API_KEY")
REDIS_URL = os.getenv("REDIS_URL")
redis_client = redis.Redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)

@app.route("/chat", methods=["POST"])
@jwt_required()
def result():
    data = request.json
    character = data.get("character", "")
    user_msg = data.get("message", "")
    document_id = data.get("document_id", "")


    print(request.method)
    print("Character", character)
    print(document_id)
    
    current_user_id = get_jwt_identity()
    user = Users.query.filter_by(id=current_user_id).first()
    
    redis_key = f"chat:{current_user_id}:{document_id}"
    
    print("REDIS KEY:", redis_key)
    
    if not user:
        return {"Error":"User not found."}
    
    if user.daily_tokens_used >= user.daily_token_limit:
        return {"Error":"Out of Token's for today."}, 429
    
    summary = redis_client.get(f"doc:{document_id}")
    
    # fetch previous chat history
    stored_messages = redis_client.lrange(redis_key, -20, -1)
    is_first_message = (len(stored_messages) == 0)
    
    chat_history = [
        json.loads(msg)
        for msg in stored_messages
    ]

    # current user message
    current_user_message = {
        "role": "user",
        "content": user_msg
    }

    # save user message to redis
    redis_client.rpush(
        redis_key,
        json.dumps(current_user_message)
    )

    # expiry timer (10 mins)
    redis_client.expire(redis_key, 600)

    def generate():

        # first message => inject note into memory once
        if is_first_message and summary:

            note_message = {
                "role": "system",
                "content": f"""
        The user is currently studying the following note.

        {summary}
        """
            }

            redis_client.rpush(
                redis_key,
                json.dumps(note_message)
            )

            # refetch updated history
            stored_messages.append(
                json.dumps(note_message)
            )
        
        info_prompt = ""
        if character == "hayasaka":
            info_prompt = """You are Hayasaka from the anime "Kaguya Sama love is war" helping a user in doubts from a note."""
        elif character == "fern":
            info_prompt = """You are Fern from the anime "Frieren" helping a user in doubts from a note."""
        elif character == "mahiru":
            info_prompt = """You are "Mahiru Shina" from the anime "Angel next door" helping a user in doubts from a note."""

        with open("core/routes/rules/prompt.txt","r", encoding="utf-8") as f:
            default_prompt = f.read()
            
        system_prompt = f"""
{info_prompt}

{default_prompt}
"""

        # full conversation sent to AI
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            *chat_history,
            current_user_message # since, current_user_message is seperated out.
        ]

        full_response = ""

        with OpenRouter(api_key=API_KEY) as client:
            total_tokens = 0

            try:
                stream = client.chat.send(
                    model="openrouter/free",
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
                        full_response += delta.content
                        yield delta.content

            except TooManyRequestsResponseError:
                yield "\n\n⚠️ The AI provider is currently rate limited. Please try again in a few moments."
                return

        # AFTER streaming ends:
        # save assistant response to redis
        assistant_message = {
            "role": "assistant",
            "content": full_response
        }

        redis_client.rpush(
            redis_key,
            json.dumps(assistant_message)
        )

        # keep only latest 20 messages
        redis_client.ltrim(redis_key, -20, -1)

        # refresh expiry again
        redis_client.expire(redis_key, 600)

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
                model="openrouter/free",
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
