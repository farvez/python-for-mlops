import csv
from pathlib import Path

file_path = Path("data/sample.csv")

def load_csv(path):
    records = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records

data = load_csv(file_path)
print(data)