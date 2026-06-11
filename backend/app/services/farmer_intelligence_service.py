from app.database.mongodb import db


def get_farmer_crop_history(
    user_id
):

    pipeline = [
        {
            "$match": {
                "user_id": user_id
            }
        },
        {
            "$group": {
                "_id": "$crop",
                "count": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "count": -1
            }
        }
    ]

    return list(
        db.chat_logs.aggregate(
            pipeline
        )
    )


def get_farmer_disease_history(
    user_id
):

    pipeline = [
        {
            "$match": {
                "user_id": user_id
            }
        },
        {
            "$group": {
                "_id": "$disease",
                "count": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "count": -1
            }
        }
    ]

    return list(
        db.chat_logs.aggregate(
            pipeline
        )
    )


def generate_farmer_recommendations(
    user_id
):

    crop_history = (
        get_farmer_crop_history(
            user_id
        )
    )

    disease_history = (
        get_farmer_disease_history(
            user_id
        )
    )

    recommendations = []

    if crop_history:

        top_crop = crop_history[0]["_id"]

        recommendations.append(
            f"Focus on preventive care for {top_crop}."
        )

    if disease_history:

        top_disease = disease_history[0]["_id"]

        recommendations.append(
            f"Monitor symptoms related to {top_disease}."
        )

    recommendations.append(
        "Check weather forecasts before irrigation."
    )

    recommendations.append(
        "Perform weekly crop health inspections."
    )

    return recommendations