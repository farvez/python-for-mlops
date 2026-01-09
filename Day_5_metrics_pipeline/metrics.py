def evaluate(metrics):
    accuracy = metrics["accuracy"]

    if accuracy >= 0.8:
        status = "APPROVED"
    else:
        status = "REJECTED"
    
    return {
        "accuracy": accuracy,
        "loss": metrics["loss"],
        "status": status
    }