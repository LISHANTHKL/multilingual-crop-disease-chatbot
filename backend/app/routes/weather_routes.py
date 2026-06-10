import os
import requests

from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


@router.get("/current")
async def get_weather(city: str):

    if not API_KEY:
        return {
            "success": False,
            "message": "OPENWEATHER_API_KEY not found"
        }

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    data = response.json()

    # Return raw response if weather data not found
    if "main" not in data:

        return {
            "success": False,
            "message": "OpenWeather Error",
            "response": data
        }

    return {
        "success": True,
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["main"]
    }

