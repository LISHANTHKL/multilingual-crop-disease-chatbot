import json

with open(
    "datasets/disease_knowledge.json",
    "r",
    encoding="utf-8"
) as file:

    KNOWLEDGE_BASE = json.load(file)


def detect_disease(query):

    query = query.lower()

    for record in KNOWLEDGE_BASE:

        for symptom in record["symptoms"]:

            if symptom.lower() in query:

                return {
                    "crop": record["crop"],
                    "disease": record["disease"],
                    "cause": record["cause"],
                    "treatment": record["treatment"],
                    "prevention": record["prevention"]
                }

    return {
        "message": "Disease not identified"
    }