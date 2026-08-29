import sqlite3
import pandas as pd


def load_to_sql():
    parquet_file = "data/gold/weather.parquet"
    database_file = "database/weather.db"

    df = pd.read_parquet(parquet_file)

    connection = sqlite3.connect(database_file)

    df.to_sql(
        "weather",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print(f"[OK] Loaded {len(df)} rows into SQLite database.")
    print(f"Database: {database_file}")
    print("Table: weather")


if __name__ == "__main__":
    load_to_sql()