import json

with open("metrics.json") as f:
    metrics = json.load(f)

print(metrics)