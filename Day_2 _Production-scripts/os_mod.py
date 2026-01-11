import os

print(os.getcwd())
print(os.listdir())

env = os.getenv("ENV", "dev")

print(f"Running in {env} environment")