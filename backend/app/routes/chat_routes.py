from fastapi import APIRouter
from app.database.database import db

router = APIRouter()


@router.get("/recent")
async def get_recent_chats():

    chats = []

    cursor = (
        db.chat_logs
        .find()
        .sort("_id", -1)
        .limit(5)
    )

    async for chat in cursor:

        chat["_id"] = str(chat["_id"])

        chats.append(chat)

    return {
        "success": True,
        "count": len(chats),
        "data": chats
    }

