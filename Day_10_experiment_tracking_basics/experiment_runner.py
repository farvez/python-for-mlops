import json
from pathlib import Path

from data_loader import load_csv
from splitter import split_data
from trainer import train_model
from evaluator import evaluate

ARTIFACTS = Path("artifacts/experiments")
ARTIFACTS.mkdir(parents=True, exist_ok=True)

def run_experiment(run_id, seed):
    X,y = load_csv("data/dataset.csv")

    X_train, X_val, y_train, y_val = split_data(X,y, seed=seed)
    model_path = ARTIFACTS / "model.pkl"

    model = train_model(X_train,y_train, model_path)
    metrics = evaluate(model, X_val, y_val)

    output = {
        "run_id": run_id,
        "seed": seed,
        "metrics": metrics
    }

    with open(ARTIFACTS / f"run_{run_id}.json", "w") as f:
        json.dump(output, f, indent =2)

def main():
    seeds = [42, 7, 99]

    for idx, seed in enumerate(seeds, start=1):
        run_experiment(idx, seed)
        print("All experiments completed")

if __name__ == "__main__":
    main()