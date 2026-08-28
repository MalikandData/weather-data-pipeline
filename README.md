# Weather Data Engineering Pipeline

An end-to-end data engineering project that collects weather data from a
REST API, processes and transforms the data, and stores it for analysis.

## Overview

The pipeline retrieves weather data from a public API and processes it
through multiple stages before making the data available for analysis.

The project demonstrates:

- API data ingestion
- Data cleaning and transformation
- Bronze, Silver and Gold data layers
- Parquet data storage
- SQL data loading
- Pipeline orchestration
- Logging and error handling
- Configuration management
- Automated pipeline execution

## Architecture

API → Ingestion → Bronze → Silver → Gold → SQL

### Pipeline Flow

1. Retrieve weather data from a REST API
2. Store the raw data in the Bronze layer
3. Clean and transform the data in the Silver layer
4. Create analysis-ready data in the Gold layer
5. Store the processed data in Parquet and SQL
6. Run the pipeline through an automated workflow

## Technologies

- Python
- SQL
- SQLite
- Parquet
- REST API
- Git

## Project Structure

```text
weather-data-pipeline/
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── src/
├── config/
├── logs/
├── main.py
├── requirements.txt
└── README.md
