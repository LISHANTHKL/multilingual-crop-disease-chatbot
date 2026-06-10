from fastapi import APIRouter
from pydantic import BaseModel

from app.services.intent_service import (
    predict_intent
)

router = APIRouter()


class IntentRequest(BaseModel):
    query: str


@router.post("/predict")
async def predict(request: IntentRequest):

    result = predict_intent(
        request.query
    )

    return result