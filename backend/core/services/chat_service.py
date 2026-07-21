import json
import os
import uuid

from dotenv import load_dotenv
import redis
from openrouter import OpenRouter
from openrouter.errors import TooManyRequestsResponseError

from core.db import Users
from main import db
from tools.helpers import DEFAULT_PROMPT, SUMMARY_PROMPT

load_dotenv()

MODEL = "openai/gpt-oss-120b"
API_KEY = os.getenv("API_KEY")

redis_client = redis.Redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)


def create_document_id():
    return str(uuid.uuid4())


def stream_chat_response(user_id, character, user_msg, document_id):
    redis_key = f"chat:{user_id}:{document_id}"
    summary = redis_client.get(f"doc:{document_id}")

    stored_messages = redis_client.lrange(redis_key, -20, -1)
    is_first_message = len(stored_messages) == 0
    chat_history = [json.loads(msg) for msg in stored_messages]

    current_user_message = {
        "role": "user",
        "content": user_msg
    }

    redis_client.rpush(redis_key, json.dumps(current_user_message))
    redis_client.expire(redis_key, 600)

    if is_first_message and summary:
        note_message = {
            "role": "system",
            "content": f"""
        The user is currently studying the following note.

        {summary}
        """
        }

        redis_client.rpush(redis_key, json.dumps(note_message))
        stored_messages.append(json.dumps(note_message))

    messages = [
        {
            "role": "system",
            "content": build_system_prompt(character)
        },
        *chat_history,
        current_user_message
    ]

    full_response = ""
    total_tokens = 0

    with OpenRouter(api_key=API_KEY) as client:
        try:
            stream = client.chat.send(
                model=MODEL,
                messages=messages,
                stream=True,
                max_tokens=1024
            )

            for event in stream:
                total_tokens += get_usage_tokens(event)
                chunk = get_event_content(event)

                if chunk:
                    full_response += chunk
                    yield chunk

        except TooManyRequestsResponseError:
            yield "\n\nWarning: The AI provider is currently rate limited. Please try again in a few moments."
            return

    save_assistant_message(redis_key, full_response)
    add_token_usage(user_id, total_tokens)


def stream_summary_response(user_id, text, document_id):
    full_summary = ""
    total_tokens = 0

    with OpenRouter(api_key=API_KEY) as client:
        stream = client.chat.send(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SUMMARY_PROMPT
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
            total_tokens += get_usage_tokens(event)
            chunk = get_event_content(event)

            if chunk:
                full_summary += chunk
                yield chunk

    add_token_usage(user_id, total_tokens)
    redis_client.setex(f"doc:{document_id}", 300, full_summary)


def build_system_prompt(character):
    character_prompts = {
        "hayasaka": 'You are Hayasaka from the anime "Kaguya Sama love is war" helping a user in doubts from a note.',
        "fern": 'You are Fern from the anime "Frieren" helping a user in doubts from a note.',
        "mahiru": 'You are "Mahiru Shina" from the anime "Angel next door" helping a user in doubts from a note.'
    }

    info_prompt = character_prompts.get(character, "")

    return f"""
{info_prompt}

{DEFAULT_PROMPT}
"""


def get_event_content(event):
    if not event.choices:
        return ""

    delta = event.choices[0].delta
    if hasattr(delta, "content") and delta.content:
        return delta.content

    return ""


def get_usage_tokens(event):
    if hasattr(event, "usage") and event.usage:
        print("TOTAL:", event.usage.total_tokens)
        return event.usage.total_tokens

    return 0


def save_assistant_message(redis_key, full_response):
    assistant_message = {
        "role": "assistant",
        "content": full_response
    }

    redis_client.rpush(redis_key, json.dumps(assistant_message))
    redis_client.ltrim(redis_key, -20, -1)
    redis_client.expire(redis_key, 600)


def add_token_usage(user_id, total_tokens):
    user = Users.query.filter_by(id=user_id).first()

    if user:
        user.daily_tokens_used += total_tokens
        db.session.commit()
