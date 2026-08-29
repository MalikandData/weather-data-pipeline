import json
import os
from datetime import datetime
import csv


def get_latest_bronze_file(bronze_folder="data/bronze"):
    if not os.path.exists(bronze_folder):
        raise FileNotFoundError(f"Bronze folder not found: {bronze_folder}")

    files = [
        f for f in os.listdir(bronze_folder)
        if f.endswith(".json")
    ]

    if not files:
        raise FileNotFoundError("No JSON files found in bronze layer.")

    files.sort()
    latest_file = files[-1]

    return os.path.join(bronze_folder, latest_file)


def load_bronze_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def clean_weather(raw_json, city_name="Copenhagen"):
    hourly = raw_json.get("hourly", {})

    times = hourly.get("time", [])
    temps = hourly.get("temperature_2m", [])

    if not times or not temps:
        raise ValueError("Missing 'time' or 'temperature_2m' in JSON.")

    if len(times) != len(temps):
        raise ValueError("Length mismatch between time and temperature lists.")

    rows = []

    for timestamp, temperature in zip(times, temps):
        rows.append({
            "timestamp": timestamp,
            "temp": temperature,
            "city": city_name
        })

    return rows


def save_to_silver(rows, silver_folder="data/silver"):
    os.makedirs(silver_folder, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"clean_{today}.csv"
    filepath = os.path.join(silver_folder, filename)

    fieldnames = ["timestamp", "temp", "city"]

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[OK] Cleaned data saved to {filepath}")


def main():
    print("Loading latest bronze file...")

    bronze_path = get_latest_bronze_file()
    print(f"Using bronze file: {bronze_path}")

    raw_json = load_bronze_json(bronze_path)

    print("Cleaning weather data into tabular format...")

    rows = clean_weather(raw_json, city_name="Copenhagen")

    print(f"Total rows: {len(rows)}")

    print("Saving to silver layer as CSV...")

    save_to_silver(rows)

    print("Silver layer updated successfully.")


if __name__ == "__main__":
    main()