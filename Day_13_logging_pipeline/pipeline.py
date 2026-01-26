import os
import json
from pathlib import Path

from data_loader import load_csv
from splitter import split_data
from trainer import train_model
from evaluator import evaluate
from validator import validate_metrics
from logger import get_logger

logger = get_logger()

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

def main():
    logger.info("Pipeline started")

    try:
        logger.info("loading data")
        X,y = load_csv("data/dataset.csv")

        logger.info("Splitting data")
        X_train, X_val, y_train, y_val = split_data(X,y, seed=42)

        logger.info("Training model")
        model_path = ARTIFACTS / "model.pkl"
        model = train_model(X_train, y_train, model_path)

        logger.info("Evaluating model")
        metrics = evaluate(model, X_val, y_val)

        logger.info("Validating metrics")
        validate_metrics(metrics, threshold=0.7)

        with open(ARTIFACTS / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)
        
        logger.info("Pipeline is completed successfully")
    
    except Exception as e:
        logger.info(f"Pipeline failed :{e}")

        with open(ARTIFACTS / "failure.txt", "w") as f:
            f.write(str(e))
        raise SystemExit(1)

if __name__ == "__main__":
    main()
