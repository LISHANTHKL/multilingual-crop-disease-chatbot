from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import (
    process_farmer_query
)

router = APIRouter()


class ChatbotRequest(BaseModel):
    query: str


@router.post("/ask")
async def ask_ai(
    request: ChatbotRequest
):

    result = process_farmer_query(
        request.query
    )

    return result