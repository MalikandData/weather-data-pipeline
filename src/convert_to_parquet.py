import os
import pandas as pd


def get_latest_silver_file(silver_folder="data/silver"):
    files = [
        f for f in os.listdir(silver_folder)
        if f.endswith(".csv")
    ]

    if not files:
        raise FileNotFoundError("No CSV files found in silver layer.")

    files.sort()
    return os.path.join(silver_folder, files[-1])


def convert_to_parquet():
    silver_file = get_latest_silver_file()

    df = pd.read_csv(silver_file)

    os.makedirs("data/gold", exist_ok=True)

    output_file = "data/gold/weather.parquet"

    df.to_parquet(output_file, index=False)

    print(f"[OK] Gold data saved to {output_file}")
    print(f"Rows: {len(df)}")


if __name__ == "__main__":
    convert_to_parquet()