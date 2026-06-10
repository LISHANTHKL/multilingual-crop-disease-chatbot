from app.services.intent_service import (
    predict_intent
)

from app.services.entity_service import (
    extract_entities
)

from app.services.disease_service import (
    detect_disease
)

from app.services.multilingual_service import (
    detect_language,
    translate_to_english,
    translate_response
)

from app.services.recommendation_service import (
    generate_recommendation
)

from rag.search_engine import (
    search_knowledge
)


def process_farmer_query(query):

    # -------------------
    # Language Detection
    # -------------------

    language = detect_language(
        query
    )

    english_query = translate_to_english(
        query
    )

    # -------------------
    # Intent
    # -------------------

    intent_result = predict_intent(
        english_query
    )

    intent = intent_result["intent"]

    # -------------------
    # Crop Detection
    # -------------------

    entity_result = extract_entities(
        english_query
    )

    crop = entity_result.get(
        "crop"
    )

    # -------------------
    # Disease Detection
    # -------------------

    disease_result = detect_disease(
        english_query
    )

    disease = disease_result.get(
        "disease"
    )

    # -------------------
    # RAG Search
    # -------------------

    rag_results = search_knowledge(
        english_query
    )

    # -------------------
    # Recommendation
    # -------------------

    recommendation = generate_recommendation(
        crop=crop,
        disease=disease
    )

    # -------------------
    # Response Builder
    # -------------------

    response = f"""
Intent: {intent}

Crop: {crop}

Disease: {disease}

Recommendations:

{chr(10).join(recommendation['recommendations'])}
"""

    translated_response = translate_response(
        response,
        language
    )

    return {
        "language": language,
        "intent": intent,
        "crop": crop,
        "disease": disease,
        "knowledge": rag_results,
        "recommendations": recommendation[
            "recommendations"
        ],
        "response": translated_response
    }