import logging
import sqlite3

import pandas as pd

from logging_config import setup_logging


def load_to_sql():
    parquet_file = "data/gold/weather.parquet"
    database_file = "database/weather.db"

    logging.info(f"Reading Parquet file: {parquet_file}")

    df = pd.read_parquet(parquet_file)

    logging.info(f"Loaded {len(df)} rows from Parquet")

    connection = sqlite3.connect(database_file)

    df.to_sql(
        "weather",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    logging.info("Weather data loaded into SQLite database")

    print(f"[OK] Loaded {len(df)} rows into SQLite database.")
    print(f"Database: {database_file}")
    print("Table: weather")


if __name__ == "__main__":
    setup_logging()

    logging.info("Starting SQL data loading")

    load_to_sql()

    logging.info("SQL data loading completed")