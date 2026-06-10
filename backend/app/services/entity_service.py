import re

# Supported Crops
CROPS = [
    "rice",
    "tomato",
    "potato",
    "wheat",
    "corn",
    "cotton",
    "banana",
    "apple",
    "grapes",
    "mango",
    "sugarcane",
    "onion",
    "chilli",
    "pepper",
    "coconut",
    "arecanut",
    "jackfruit",
    "cashew"
]


def extract_entities(text: str):

    text_lower = text.lower()

    detected_crop = None

    for crop in CROPS:

        pattern = rf"\b{re.escape(crop)}\b"

        if re.search(pattern, text_lower):

            detected_crop = crop.title()
            break

    return {
        "query": text,
        "crop": detected_crop,
        "entity_found": detected_crop is not None,
        "confidence": 1.0 if detected_crop else 0.0
    }