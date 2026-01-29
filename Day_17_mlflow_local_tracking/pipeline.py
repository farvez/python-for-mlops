import mlflow
import mlflow.sklearn
from train import train

def main():
    # tracking_uri = "sqlite:///mlflow.db" # Using SQLite is more stable than folders
    # mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment("credit-approval-mlops")

    with mlflow.start_run():
        model, accuracy, seed = train()

        #log params
        mlflow.log_param("seed", seed)
        mlflow.log_param("model_type", "LogisticRegression")

        #log metrics
        mlflow.log_metric("validation_accuracy", accuracy)

        #log model artifacts
        mlflow.sklearn.log_model(model, "model")

        print("RUN completed with accuracy:", accuracy)


if __name__ == "__main__":
    main()