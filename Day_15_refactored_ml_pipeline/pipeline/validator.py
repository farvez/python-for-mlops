def validate_metrics(metrics, threshold=0.7):
    acc = metrics["validation_accuracy"]
    if acc < threshold:
        raise ValueError(
            f"Validation accuracy {acc} is below threshold {threshold}"
        )
