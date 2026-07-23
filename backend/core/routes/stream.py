from flask import Response, request, stream_with_context
from flask_jwt_extended import get_jwt_identity, jwt_required
from core.db import VoiceLine

from core.services.chat_service import (
    create_document_id,
    stream_chat_response,
    stream_summary_response,
)
from core.services.route_helper import validate_user
from main import app


@app.route("/chat", methods=["POST"])
@jwt_required()
def result():
    data = request.json or {}
    current_user_id = get_jwt_identity()

    _, error_response = validate_user(current_user_id)
    if error_response:
        return error_response

    response_stream = stream_chat_response(
        user_id=current_user_id,
        character=data.get("character", ""),
        user_msg=data.get("message", ""),
        document_id=data.get("document_id", "")
    )

    return Response(
        stream_with_context(response_stream),
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
    data = request.json or {}
    text = data.get("text", "")

    if not text:
        return {"error": "No text provided"}, 400

    current_user_id = get_jwt_identity()
    _, error_response = validate_user(current_user_id, reset_tokens=True)
    if error_response:
        return error_response

    document_id = create_document_id()
    response_stream = stream_summary_response(
        user_id=current_user_id,
        text=text,
        document_id=document_id
    )

    return Response(
        stream_with_context(response_stream),
        mimetype="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "X-Document-ID": document_id
        }
    )
