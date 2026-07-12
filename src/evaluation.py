from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent
METRICS_PATH = PROJECT_ROOT / "reports" / "metrics.json"


def load_metrics():
    """Load model evaluation metrics."""
    with open(METRICS_PATH, "r") as file:
        return json.load(file)