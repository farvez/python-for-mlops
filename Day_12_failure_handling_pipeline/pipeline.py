import json
from pathlib import Path
from data_loader import load_csv
from splitter import split_data
from trainer import train_model
from evaluator import evaluate
from validator import validate_metrics

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)
def main ():

    try:
        X,y = load_csv("data/dataset.csv")

        X_train, X_val, y_train, y_val = split_data(X,y, seed=42)

        model_path = ARTIFACTS / "model.pkl"

        model = train_model(X_train, y_train, model_path)
        metrics = evaluate(model, X_val, y_val)

        #quality gate
        validate_metrics(metrics, threshold = 1.7)

        with open(ARTIFACTS / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)

        print("pipeline is competed successfully")

    except Exception as e:

        with open(ARTIFACTS / "failure.txt", "w") as f:
            f.write(str(e))
        
        print("pipeline failed")
        raise SystemExit(1)

if __name__ == "__main__":
    main()