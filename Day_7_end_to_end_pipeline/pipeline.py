import json
import logging
from pathlib import Path
from pyexpat import features

from data_loader import load_csv
from validator import validate_data, validate_schema
from feature_engineering import prepare_features
from splitter import train_val_split
from trainer import train_model
from metrics import evaluate
from artifact_writer import write_csv

logging.basicConfig(level=logging.INFO)

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

def main():
    logging.info("Pipeline Started")

    #load_data
    data = load_csv("data/sample.csv")
    #validate
    errors = validate_data(data)+validate_schema(data)
    if errors:
        logging.error("Data validation failed")
        for err in errors:
            logging.err(err)
        raise SystemExit(1)
    #feature preparation
    features = prepare_features(data)

    #split
    train, val = train_val_split(features)

    #save dataset
    write_csv(train, ARTIFACTS / "train.csv")
    write_csv(val, ARTIFACTS / "val.csv")

    #train(simulate)
    raw_metrics = train_model(seed=42)

    #evaluate
    final_metrics = evaluate(raw_metrics, threshold=0.8)

    #write artifacts

    with open(ARTIFACTS / "metrics.json", "w") as f:
        json.dump(final_metrics, f, indent=2)
    
    with open(ARTIFACTS / "status.txt", "w") as f:
        f.write(final_metrics["status"])
    
    logging.info(f"pipeline completed with status: {final_metrics['status']}")


if __name__ == "__main__":
    main()
