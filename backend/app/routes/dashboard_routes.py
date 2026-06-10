from fastapi import APIRouter
from app.database.database import db

router = APIRouter()

@router.get("/stats")
async def get_dashboard_stats():

    total_users = await db.users.count_documents({})

    total_chats = await db.chat_logs.count_documents({})

    total_reports = await db.reports.count_documents({})

    total_predictions = await db.disease_predictions.count_documents({})

    return {
        "totalUsers": total_users,
        "totalChats": total_chats,
        "totalReports": total_reports,
        "totalPredictions": total_predictions
    }