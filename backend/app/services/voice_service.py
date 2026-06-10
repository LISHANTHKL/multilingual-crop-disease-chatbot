import edge_tts
import uuid
import os

AUDIO_FOLDER = "audio"

os.makedirs(
    AUDIO_FOLDER,
    exist_ok=True
)

async def text_to_speech(
    text,
    language="en"
):

    voices = {
        "en": "en-US-AriaNeural",
        "hi": "hi-IN-SwaraNeural",
        "kn": "kn-IN-SapnaNeural"
    }

    voice = voices.get(
        language,
        "en-US-AriaNeural"
    )

    filename = f"{uuid.uuid4()}.mp3"

    filepath = os.path.join(
        AUDIO_FOLDER,
        filename
    )

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(
        filepath
    )

    return filepath