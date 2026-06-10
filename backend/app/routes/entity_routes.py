from fastapi import APIRouter
from pydantic import BaseModel

from app.services.entity_service import (
    extract_entities
)

router = APIRouter()


class EntityRequest(BaseModel):
    query: str


@router.post("/extract")
async def extract(request: EntityRequest):

    result = extract_entities(
        request.query
    )

    return result