from fastapi import APIRouter

from app.services.intelligence_service import (
    get_crop_insights,
    get_disease_insights,
    generate_agriculture_insights
)

router = APIRouter()


@router.get("/insights")
async def get_insights():

    return {
        "topCrops":
        get_crop_insights(),

        "topDiseases":
        get_disease_insights(),

        "insights":
        generate_agriculture_insights()
    }