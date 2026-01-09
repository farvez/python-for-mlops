import json
import logging
from pathlib import Path
from trainer import train_model
from metrics import evaluate


logging.basicConfig(level=logging.INFO)

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

train_data = Path("data/train.csv")

raw_metrics = train_model(train_data)
final_metrics =evaluate(raw_metrics)

with open(ARTIFACTS / "metrics.json", "w") as f:
    json.dump(final_metrics, f, indent=2)

with open(ARTIFACTS / "status.txt", "w") as f:
    f.write(final_metrics["status"])

logging.info(f"Training status: {final_metrics['status']}")
logging.info("Training piepline is completed")