import csv

def load_data(path):
    X, y = [], []

    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            X.append([int(row["age"]), int(row["salary"])])
            y.append(int(row["label"]))
    return X, y

# if __name__ == "__main__":
#     path = "C:\\Users\\Admin\\Downloads\\Python for MLOps\\Day_8_real_ml_pipeline\\data\\dataset.csv"

#     cat = load_data(path)
#     print(cat)