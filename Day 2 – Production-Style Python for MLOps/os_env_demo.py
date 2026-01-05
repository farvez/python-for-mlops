import os 
env = os.getenv("ENV", "dev")

print(f"Running in {env} environment")

# Used in:
# SageMaker
# Docker
# GitHub Actions