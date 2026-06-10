from langdetect import detect
from deep_translator import GoogleTranslator


def detect_language(text):

    try:

        language = detect(text)

        return language

    except Exception:

        return "en"


def translate_to_english(text):

    try:

        translated = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        return translated

    except Exception:

        return text


def translate_response(
    text,
    target_language
):

    try:

        translated = GoogleTranslator(
            source="en",
            target=target_language
        ).translate(text)

        return translated

    except Exception:

        return text