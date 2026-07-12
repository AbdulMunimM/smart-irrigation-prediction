from src.model import load_model
from src.evaluation import load_metrics

model = load_model()
metrics = load_metrics()

print("Model loaded successfully!")
print(metrics)