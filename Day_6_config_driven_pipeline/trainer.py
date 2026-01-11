import random

def train_seed(seed):
    random.seed(seed)

    accuracy = round(random.uniform(0.7, 0.9), 2)
    loss = round(random.uniform(03, 0.6), 2)

    return {
        "accuracy": accuracy,
        "loss": loss
    }