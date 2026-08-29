import json
import os
from datetime import datetime

import requests


def fetch_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=55.6761"
        "&longitude=12.5683"
        "&hourly=temperature_2m"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def save_to_bronze(weather_data):
    os.makedirs("data/bronze", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"data/bronze/weather_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(weather_data, file, indent=2)

    print(f"Weather data saved to: {file_path}")


if __name__ == "__main__":
    weather_data = fetch_weather()
    save_to_bronze(weather_data)