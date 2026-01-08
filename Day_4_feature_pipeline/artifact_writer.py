import csv
from pathlib import Path

def write_csv(data, path):
    path.parent.mkdir(exist_ok=True)

    with open(path, "w", newline="")as f:
        writer = csv.DictWriter(f,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)