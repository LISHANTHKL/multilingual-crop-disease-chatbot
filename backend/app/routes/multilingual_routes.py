from fastapi import APIRouter
from pydantic import BaseModel

from app.services.multilingual_service import (
    detect_language,
    translate_to_english,
    translate_response
)

router = APIRouter()


class TranslationRequest(BaseModel):
    query: str


@router.post("/process")
async def process_query(
    request: TranslationRequest
):

    detected_language = detect_language(
        request.query
    )

    english_query = translate_to_english(
        request.query
    )

    translated_back = translate_response(
        english_query,
        detected_language
    )

    return {
        "detected_language": detected_language,
        "english_query": english_query,
        "translated_response": translated_back
    }