import json
from pathlib import Path
from data_loader import load_csv
from splitter import split_data
from evaluator import evaluate
from trainer import train_model

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

def main():

    X,y = load_csv("data/dataset.csv")

    X_train,X_val,y_train,y_val = split_data(X,y)
    print(f"Total samples: {len(X)}")
    print(f"Training labels distribution: {set(y_train)}")
    print(f"Validation labels distribution: {set(y_val)}")

    model_path = ARTIFACTS / "model.pkl"
    model = train_model(X_train, y_train, model_path)

    metrics = evaluate(model, X_val, y_val)
    print(f"Actual labels: {y_val}")

    with open(ARTIFACTS / "metrics.json" , "w") as f:
        json.dump(metrics, f, indent=2)
    
    print("pipeline completed")
    print(metrics)

if __name__ == "__main__":
    main()