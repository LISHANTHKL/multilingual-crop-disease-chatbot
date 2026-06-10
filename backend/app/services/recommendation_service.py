def generate_recommendation(
    crop,
    disease,
    weather=None,
    temperature=None,
    humidity=None
):

    recommendations = []

    # Disease Recommendations

    if disease:

        recommendations.append(
            f"Monitor {crop} crop closely for {disease} progression."
        )

        recommendations.append(
            "Follow recommended fungicide or pesticide schedule."
        )

        recommendations.append(
            "Remove heavily infected plant parts."
        )

    # Weather Recommendations

    if weather:

        weather = weather.lower()

        if "rain" in weather:

            recommendations.append(
                "Reduce irrigation due to expected rainfall."
            )

            recommendations.append(
                "Inspect crops for fungal infections after rain."
            )

        if "clear" in weather:

            recommendations.append(
                "Suitable conditions for field inspection."
            )

        if "cloud" in weather:

            recommendations.append(
                "Monitor humidity-sensitive diseases."
            )

    # Humidity Recommendations

    if humidity:

        if humidity > 80:

            recommendations.append(
                "High humidity may increase fungal disease risk."
            )

        elif humidity < 40:

            recommendations.append(
                "Low humidity may require additional irrigation."
            )

    # Temperature Recommendations

    if temperature:

        if temperature > 35:

            recommendations.append(
                "High temperature stress detected. Increase crop monitoring."
            )

        elif temperature < 15:

            recommendations.append(
                "Low temperature may slow crop growth."
            )

    return {
        "crop": crop,
        "disease": disease,
        "weather": weather,
        "temperature": temperature,
        "humidity": humidity,
        "recommendations": recommendations
    }