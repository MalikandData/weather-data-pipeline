import logging
import subprocess

from logging_config import setup_logging


def run_step(step_name, command):
    logging.info(f"Starting step: {step_name}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        logging.error(f"Step failed: {step_name}")
        logging.error(result.stderr)
        raise RuntimeError(f"{step_name} failed.")

    logging.info(f"Completed step: {step_name}")
    print(f"[OK] {step_name}")


def main():
    setup_logging()

    logging.info("Starting weather data pipeline")

    steps = [
        ("Weather API ingestion", ["py", "src/fetch_weather.py"]),
        ("Weather transformation", ["py", "src/transform_weather.py"]),
        ("Parquet conversion", ["py", "src/convert_to_parquet.py"]),
        ("SQL loading", ["py", "src/load_to_sql.py"])
    ]

    for step_name, command in steps:
        run_step(step_name, command)

    logging.info("Weather data pipeline completed successfully")
    print("\n[OK] Full weather pipeline completed.")


if __name__ == "__main__":
    main()