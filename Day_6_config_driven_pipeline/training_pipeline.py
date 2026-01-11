import argparse
import json
import logging
from pathlib import Path
from config_loader import load_config
from trainer import train_model
from metrics import evaluate

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()

config = load_config(args.config)

ARTIFACTS = Path("artifacts/experiment_outputs")
ARTIFACTS.mkdir(parents=True, exist_ok=True)

logging.info(f"Running experiment : {config['experiment_name']}")

raw_metrics = train_model(config["random_seed"])
final_metrics = evaluate(raw_metrics, config["accuracy_threshold"])

output = {
    "experiment": config["experiment_name"],
    "config": config,
    "metrics": final_metrics
}

output_file = ARTIFACTS / f"{config['experiment_name']}.json"

with open(output_file, "w") as f:
    json.dump(output, f, indent=2)

logging.info(f"Experiment resutl saved to {output_file}")