from sklearn.linear_model import LogisticRegression
import joblib

def train_model(X, y, model_path):
    model = LogisticRegression()
    model.fit(X,y)

    joblib.dump(model, model_path)
    return model