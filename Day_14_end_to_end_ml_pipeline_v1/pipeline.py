import json
from pathlib import Path

from data_loader import load_data
from splitter import split_data
from trainer import train_model
from evaluator import evaluate
from logger import get_logger
from validator import validate_metrics

logger = get_logger()
ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

def main():
    logger.info("Pipeline started")
    try:
        

        logger.info("Loading data")
        X, y = load_data("data/dataset.csv")

        logger.info("splitting data(reproducible)")
        X_train, X_val, y_train, y_val = split_data(X, y, seed=42)

        logger.info("training model")
        model_path = ARTIFACTS / "model.pkl"

        model = train_model(X_train, y_train, model_path)

        logger.info("evalauting model on validation data")
        metrics = evaluate(model, X_val, y_val)

        logger.info("Applying qulity gate")
        validate_metrics(metrics, threshold=1.7)

        with open(ARTIFACTS / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)
        
        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error("Pipeline failed : {e}")
        with open(ARTIFACTS / "faliure.txt", "w") as f:
            f.write(str(e))

            raise SystemExit(1)

if __name__ == "__main__":
    main()
