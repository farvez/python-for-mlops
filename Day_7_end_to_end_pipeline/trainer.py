import random

def train_model(train_data, seed=42):
    random.seed(seed)

    #simulate training accuracy
    accuracy = round(random.uniform(0.7, 0.9), 2)
    loss = round(random.uniform(0.3, 0.6), 2)

    return{
        "accuracy": accuracy,
        "loss": loss
    }