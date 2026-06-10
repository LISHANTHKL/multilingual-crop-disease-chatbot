from fastapi import APIRouter
from pydantic import BaseModel

from app.services.disease_service import (
    detect_disease
)

router = APIRouter()


class DiseaseRequest(BaseModel):
    query: str


@router.post("/predict")
async def predict_disease(
    request: DiseaseRequest
):

    result = detect_disease(
        request.query
    )

    return result