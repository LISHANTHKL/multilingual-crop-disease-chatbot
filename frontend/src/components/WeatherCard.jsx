import { useEffect, useState } from "react";
import { getWeather } from "../services/weatherService";

export default function WeatherCard() {

  const [weather, setWeather] = useState(null);

  useEffect(() => {

    const loadWeather = async () => {

      try {

        const data = await getWeather("Madikeri");

        setWeather(data);

      } catch (error) {

        console.error(error);

      }

    };

    loadWeather();

  }, []);

  if (!weather) {

    return (
      <div className="weather-card p-4">
        Loading Weather...
      </div>
    );

  }

  return (
    <div className="weather-card p-4">

      <h4>Weather Intelligence</h4>

      <h1 className="mt-3">
        {weather.temperature}°C
      </h1>

      <p>
        {weather.city}
      </p>

      <hr />

      <p>
        Humidity: {weather.humidity}%
      </p>

      <p>
        Wind Speed: {weather.wind_speed}
      </p>

      <p>
        Condition: {weather.condition}
      </p>

    </div>
  );
}