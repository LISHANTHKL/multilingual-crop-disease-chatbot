from fastapi import APIRouter
from pydantic import BaseModel

from rag.search_engine import (
    search_knowledge
)

router = APIRouter()


class SearchRequest(BaseModel):
    query: str


@router.post("/search")
async def rag_search(
    request: SearchRequest
):

    results = search_knowledge(
        request.query
    )

    return {
        "results": results
    }