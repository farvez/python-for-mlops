import yaml

df load_config(path):
with open(path) as f:
    return yamal.safe_load(f)