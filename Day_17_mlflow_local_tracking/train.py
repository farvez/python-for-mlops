import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import csv
from pathlib import Path


def load_data(path):

    X, y = [], []

    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            X.append([int(row["age"]), int(row["salary"])])
            y.append([int(row["label"])])
        return X, y

def train():

    X, y = load_data("data/dataset.csv")
    seed=42

    X_train, X_val, y_train, y_val = train_test_split(
        X,y, test_size=0.2, random_state=seed
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_val)
    acc = accuracy_score(y_val, preds)

    return model, acc, seed

