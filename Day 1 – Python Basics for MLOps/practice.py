import yaml

with open("C:\\Users\\Admin\\Downloads\\Python for MLOps\\Day-1\\config.yaml", 'r') as f:
    config = yaml.safe_load(f)

print(f"Model type: {config['model_type']}")
print(f"Number of estimators: {config['n_estimators']}")