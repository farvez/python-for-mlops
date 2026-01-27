import csv

def load_data(path):

    X, y = [], []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            X.append([int(row["age"]), int(row["salary"])])
            y.append(int(row["label"]))
    return X,y
