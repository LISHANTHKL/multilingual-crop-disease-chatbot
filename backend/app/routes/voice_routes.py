from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.services.voice_service import (
    text_to_speech
)

router = APIRouter()


class VoiceRequest(BaseModel):

    text: str
    language: str = "en"


@router.post("/speak")
async def speak(
    request: VoiceRequest
):

    file_path = await text_to_speech(
        request.text,
        request.language
    )

    return FileResponse(
        file_path,
        media_type="audio/mpeg",
        filename="speech.mp3"
    )