@echo off

cd /d "C:\Users\Dell\Documents\Projects\weather-data-pipeline"

call .venv\Scripts\activate.bat

py src\pipeline.py
