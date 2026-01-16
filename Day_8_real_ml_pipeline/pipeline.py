import json
from pathlib  import Path
from data_loader import load_data
from trainer import train_model
from evaluator import evaluate

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)


def main():
    X, y = load_data("data/dataset.csv")

    model_path = ARTIFACTS / "model.pkl"

    model = train_model(X, y, model_path)

    metrics = evaluate(model, X, y)

    with open(ARTIFACTS / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("pipeline completed")
    print(metrics)


if __name__ == "__main__":
    main()