from app.database.mongodb import db


def get_recent_conversations(limit=10):

    chats = list(
        db.chat_logs.find(
            {},
            {
                "_id": 0,
                "user_id": 1,
                "query": 1,
                "crop": 1,
                "disease": 1,
                "timestamp": 1
            }
        )
        .sort("timestamp", -1)
        .limit(limit)
    )

    return chats


def get_top_crops():

    pipeline = [
        {
            "$group": {
                "_id": "$crop",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 5
        }
    ]

    return list(
        db.chat_logs.aggregate(
            pipeline
        )
    )


def get_top_diseases():

    pipeline = [
        {
            "$group": {
                "_id": "$disease",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 5
        }
    ]

    return list(
        db.chat_logs.aggregate(
            pipeline
        )
    )


def get_most_active_user():

    pipeline = [
        {
            "$group": {
                "_id": "$user_id",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 1
        }
    ]

    result = list(
        db.chat_logs.aggregate(
            pipeline
        )
    )

    return result[0] if result else {}
from datetime import datetime
def get_crop_distribution():

    pipeline = [
        {
            "$group": {
                "_id": "$crop",
                "count": {"$sum": 1}
            }
        }
    ]

    return list(
        db.chat_logs.aggregate(
            pipeline
        )
    )


def get_disease_distribution():

    pipeline = [
        {
            "$group": {
                "_id": "$disease",
                "count": {"$sum": 1}
            }
        }
    ]

    return list(
        db.chat_logs.aggregate(
            pipeline
        )
    )


def get_daily_chat_activity():

    pipeline = [
        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": "%Y-%m-%d",
                        "date": "$timestamp"
                    }
                },
                "count": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "_id": 1
            }
        }
    ]

    return list(
        db.chat_logs.aggregate(
            pipeline
        )
    )

