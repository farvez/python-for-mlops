def validate_metrics(metrics, threshold):
    if metrics["validation_accuracy"] < threshold:
        raise ValueError(
            f"validation accuracy {metrics['validation_accuracy']}"
            f"is below threshold {threshold}"
        )