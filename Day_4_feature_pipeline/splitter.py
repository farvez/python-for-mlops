import random

def train_val_split(data, val_ratio=0.2, seed=42):
    random.seed(seed)
    shuffled = data.copy()
    random.shuffle(shuffled)

    split_index = int(len(shuffled) * (1 - val_ratio))
    train = shuffled[:split_index]
    val = shuffled[split_index:]
    return train, val