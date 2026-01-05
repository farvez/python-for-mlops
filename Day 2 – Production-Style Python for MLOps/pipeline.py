import argparse
import os
from pathlib import Path
import logging

#logging
logging.basicConfig(
    level= logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

#arguments
parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True)
parser.add_argument("--accuracy", type=float, required=True)

args = parser.parse_args()

#pipeline logic
logging.info("pipeline started")

output_dir = Path("artifacts")
output_dir.mkdir(exist_ok=True)

if args.accuracy >= 0.8:
    status = "Approved"
else:
    status = "Rejected"

with open(output_dir / "status.txt", 'w') as f:
    f.write(status)

logging.info(f"Model {args.model} status: {status}")
logging.info("pipeline completed")