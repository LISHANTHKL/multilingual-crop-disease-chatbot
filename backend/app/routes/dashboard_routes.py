from fastapi import APIRouter

from app.database.mongodb import db

from app.services.dashboard_service import (
    get_recent_conversations,
    get_top_crops,
    get_top_diseases,
    get_most_active_user,
    get_crop_distribution,
    get_disease_distribution,
    get_daily_chat_activity
)

router = APIRouter()


@router.get("/stats")
async def dashboard_stats():

    total_users = db.users.count_documents({})
    total_chats = db.chat_logs.count_documents({})
    
    top_crops = get_top_crops()

    top_diseases = get_top_diseases()

    active_user = get_most_active_user()
    cropDistribution =get_crop_distribution()

    diseaseDistribution =get_disease_distribution()

    dailyActivity =get_daily_chat_activity()


    return {
        "totalUsers": total_users,
        "totalChats": total_chats,
        "topCrops": top_crops,
        "topDiseases": top_diseases,
        "mostActiveUser": active_user,
      "cropDistribution": cropDistribution,
        "diseaseDistribution": diseaseDistribution,
        "dailyActivity": dailyActivity


    }


@router.get("/recent-conversations")
async def recent_conversations():

    data = get_recent_conversations()

    return {
        "count": len(data),
        "conversations": data
    }
