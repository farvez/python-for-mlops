import logging
from pathlib import Path
from data_loader import load_csv
from validator import validate_data, validate_schema

logging.basicConfig(level=logging.INFO)

ARTIFATCS = Path("artifacts")
ARTIFATCS.mkdir(exist_ok=True)

data = load_csv("data/sample.csv")

schema_errors =validate_schema(data)
data_errors = validate_data(data)
all_errors = schema_errors + data_errors

if all_errors:
    report = ARTIFATCS / "data_quality_report.txt"

    with open(report, "w") as f:
        for err in all_errors:
            f.write(err + "\n")

    logging.error("Data quality check failed")
    raise SystemExit(1)

logging.INFO("Data quality check passed")

