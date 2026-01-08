import logging
from pathlib import Path
from data_loader import load_csv
from validator import validate_schema, validate_data
from feature_engineering import prepare_features
from splitter import train_val_split
from artifact_writer import write_csv

logging.basicConfig(level=logging.INFO)

ARTIFACTS = Path("artifacts")
logging.info("Dataset pipeline started")

data = load_csv("data/sample.csv")

errors = validate_schema(data) + validate_data(data)

if errors:
    logging.error("Data validation failed")
    raise SystemExit(1)

features = prepare_features(data)
train, val = train_val_split(features)

write_csv(train, ARTIFACTS / "train.csv")
write_csv(val, ARTIFACTS / "val.csv")

logging.info("Dataset pipeline completed successfully")