import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True)
parser.add_argument("--epochs", type=int, default=1)

args = parser.parse_args()

print(args.model)
print(args.epochs)

# 📌 Used in:
# SageMaker training
# Batch inference
# Airflow jobs
# CI/CD