import json

with open("C:\\Users\\Admin\\Downloads\\Python for MLOps\\Day-1\\metrics.json", 'r') as f:
    metrics = json.load(f)

print(f"Model accuracy: {metrics['accuracy']}")