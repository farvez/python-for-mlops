import json
from pathlib import Path
from data_loader import load_csv
from splitter import split_data
from trainer import train_model
from evaluator import evaluate

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

def run_pipeline(seed, output_name):
    X,y = load_csv("data/dataset.csv")

    X_train, X_val, y_train, y_val = split_data(X, y, seed=seed)
    model_path = ARTIFACTS / "model.pkl"

    model = train_model(X_train, y_train, model_path)
    metrics = evaluate(model, X_val, y_val)

    output = {
        "seed": seed,
        "metrics": metrics
    }

    with open(ARTIFACTS / output_name, "w") as f:
        json.dump(output, f, indent=2)
    
def main():
    run_pipeline(seed=42, output_name="run_seed_42.json")
    run_pipeline(seed=42, output_name="run_seed_42_repeat.json")
    run_pipeline(seed=99, output_name="run_seed_99.json")

    print("Both runs completed")

if __name__ == "__main__":
    main()   