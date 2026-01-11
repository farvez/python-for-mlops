from pathlib import Path

# ❌ Bad practice:
# file = "data/results/output.txt"

# ✅ Correct practice:

base_dir = Path.cwd()
output_dir = base_dir / "data" / "results"

output_dir.mkdir(parents=True, exist_ok=True)
file_path = output_dir / "metrics.txt"
# print(base_dir)