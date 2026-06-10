from fastapi import APIRouter
from app.database.database import db

router = APIRouter()


@router.get("/{email}")
async def get_profile(email: str):

    user = await db.users.find_one(
        {"email": email},
        {"password": 0}
    )

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    user["_id"] = str(user["_id"])

    return {
        "success": True,
        "data": user
    }

