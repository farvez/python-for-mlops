config = {}

with open("C:\\Users\\Admin\\Downloads\\Python for MLOps\\Day-1\\config.txt") as f:
    for line in f:
        key, value = line.strip().split("=")
        config[key] = value

print(config)
