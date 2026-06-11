from datetime import datetime
from app.database.mongodb import db


def save_chat_log(
    user_id,
    query,
    intent,
    crop,
    disease,
    response
):

    chat_data = {
        "user_id": user_id,
        "query": query,
        "intent": intent,
        "crop": crop,
        "disease": disease,
        "response": response,
        "timestamp": datetime.utcnow()
    }

    result = db.chat_logs.insert_one(
        chat_data
    )

    return str(
        result.inserted_id
    )


def get_user_chat_history(
    user_id
):

    chats = list(
        db.chat_logs.find(
            {"user_id": user_id},
            {"_id": 0}
        ).sort(
            "timestamp",
            -1
        )
    )

    return chats

