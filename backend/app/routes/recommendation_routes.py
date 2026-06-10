from fastapi import APIRouter
from pydantic import BaseModel

from app.services.recommendation_service import (
    generate_recommendation
)

router = APIRouter()


class RecommendationRequest(BaseModel):

    crop: str
    disease: str

    weather: str | None = None
    temperature: float | None = None
    humidity: float | None = None


@router.post("/generate")
async def generate(
    request: RecommendationRequest
):

    result = generate_recommendation(
        crop=request.crop,
        disease=request.disease,
        weather=request.weather,
        temperature=request.temperature,
        humidity=request.humidity
    )

    return result