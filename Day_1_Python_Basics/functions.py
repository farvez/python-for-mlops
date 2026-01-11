def validate_accuracy(acc, threshold=0.8):
    if acc >= threshold:
        return True
    return False

print(validate_accuracy(0.82))
