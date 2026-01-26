from sklearn.metrics import accuracy_score

def evaluate(model, X_val, y_val):

    predictions = model.predict(X_val)
    accuracy = accuracy_score(y_val, predictions)

    return {
        "validation_accuracy": round(accuracy, 2)
    }