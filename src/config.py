from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "irrigation_prediction.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# App information
APP_TITLE = "🌱 Smart Irrigation Need Prediction"

APP_DESCRIPTION = """
AI-powered decision support system for predicting irrigation
requirements using soil, weather, and crop information.
"""

AUTHOR = "Abdul Munim"

MODEL_NAME = "Decision Tree Classifier"

VERSION = "1.0"