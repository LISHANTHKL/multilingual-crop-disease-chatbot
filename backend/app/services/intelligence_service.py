from app.database.mongodb import db


def get_crop_insights():

    pipeline = [
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


def get_disease_insights():

    pipeline = [
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


def generate_agriculture_insights():

    crops = get_crop_insights()

    diseases = get_disease_insights()

    insights = []

    if crops:

        top_crop = crops[0]

        insights.append(
            f"Most discussed crop is {top_crop['_id']} with {top_crop['count']} queries."
        )

    if diseases:

        top_disease = diseases[0]

        insights.append(
            f"Most common disease is {top_disease['_id']} with {top_disease['count']} reports."
        )

    if len(crops) >= 3:

        insights.append(
            "Farmers are actively seeking crop health guidance across multiple crops."
        )

    if len(diseases) >= 3:

        insights.append(
            "Disease diversity is increasing. Preventive monitoring is recommended."
        )

    return insights