import json
import logging
import os
from datetime import datetime

import requests

from logging_config import setup_logging


def fetch_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=55.6761"
        "&longitude=12.5683"
        "&hourly=temperature_2m"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        logging.info("Weather data retrieved successfully")
        return response.json()

    except requests.RequestException as error:
        logging.error(f"Failed to retrieve weather data: {error}")
        return None


def save_to_bronze(weather_data):
    if weather_data is None:
        logging.warning("No weather data to save")
        return

    os.makedirs("data/bronze", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"data/bronze/weather_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(weather_data, file, indent=2)

    logging.info(f"Weather data saved to {file_path}")
    print(f"Weather data saved to: {file_path}")


if __name__ == "__main__":
    setup_logging()

    logging.info("Starting weather data ingestion")

    weather_data = fetch_weather()
    save_to_bronze(weather_data)

    logging.info("Weather data ingestion completed")