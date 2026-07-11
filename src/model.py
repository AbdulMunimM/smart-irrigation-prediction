from pathlib import Path
import joblib

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "best_model.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict(model, input_data):
    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data).max()

    return prediction, confidence