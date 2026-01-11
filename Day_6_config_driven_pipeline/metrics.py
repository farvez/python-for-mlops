def evaluate(metrics, threshold):
    status = "APPROVED" if metrics["accuracy"] >= threshold else "REJECTED"

    return{
        "accuracy": metrics["accuracy"],
        "loss": metrics["loss"],
        "status": status
    }