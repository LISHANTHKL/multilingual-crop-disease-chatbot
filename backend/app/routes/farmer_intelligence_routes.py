from fastapi import APIRouter

from app.services.farmer_intelligence_service import (
    get_farmer_crop_history,
    get_farmer_disease_history,
    generate_farmer_recommendations
)

router = APIRouter()


@router.get(
    "/recommendations/{user_id}"
)
async def recommendations(
    user_id: str
):

    return {

        "cropHistory":
        get_farmer_crop_history(
            user_id
        ),

        "diseaseHistory":
        get_farmer_disease_history(
            user_id
        ),

        "recommendations":
        generate_farmer_recommendations(
            user_id
        )
    }