from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import (
    process_farmer_query
)

from app.services.chat_log_service import (
    save_chat_log,
    get_user_chat_history
)

router = APIRouter()


class ChatbotRequest(BaseModel):
    query: str
    user_id: str = "guest_user"


@router.post("/ask")
async def ask_ai(
    request: ChatbotRequest
):

    result = process_farmer_query(
        request.query
    )

    save_chat_log(
        user_id=request.user_id,
        query=request.query,
        intent=result.get("intent"),
        crop=result.get("crop"),
        disease=result.get("disease"),
        response=result.get("response")
    )

    return result


@router.get("/history/{user_id}")
async def get_history(
    user_id: str
):

    history = get_user_chat_history(
        user_id
    )

    return {
        "user_id": user_id,
        "total_chats": len(history),
        "history": history
    }

