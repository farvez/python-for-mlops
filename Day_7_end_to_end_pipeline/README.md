## Day 7 – End-to-End Python MLOps Pipeline (Foundation Capstone)

### Objective
Build a single, end-to-end MLOps pipeline that connects all previous stages:
data ingestion, validation, feature preparation, training simulation, metric evaluation, and artifact generation.

This day focuses on **pipeline composition**, not new concepts.

---

### What I Practiced
- Composing multiple pipeline stages into one execution flow
- Reusing previously built, tested components
- Running the entire pipeline using a single entrypoint script
- Generating final artifacts that represent pipeline outputs
- Structuring code for clarity and explainability

---

### Why This Matters in MLOps
- Real MLOps systems orchestrate many independent stages
- Pipelines must be executable with a single command
- Clear separation of responsibilities improves maintainability
- Artifacts are the primary outputs of ML systems

---

### Folder Structure

```text
day07_end_to_end_pipeline/
│
├── data/
│ └── sample.csv
│
├── artifacts/
│ ├── train.csv
│ ├── val.csv
│ ├── metrics.json
│ └── status.txt
│
├── data_loader.py
├── validator.py
├── feature_engineering.py
├── splitter.py
├── artifact_writer.py
├── trainer.py
├── metrics.py
├── pipeline.py # Single pipeline entrypoint
└── README.md
```

---

### Pipeline Flow
1. Load raw data from CSV
2. Validate schema and data quality
3. Prepare features from validated data
4. Split dataset into training and validation sets
5. Simulate model training
6. Evaluate metrics against a threshold
7. Write pipeline artifacts (datasets, metrics, status)

---

### How to Run
```bash
python pipeline.py
This single command executes the entire pipeline.
```
---
### Pipeline Outputs

The pipeline generates the following artifacts:

train.csv and val.csv – prepared datasets

metrics.json – training and evaluation metrics

status.txt – approval or rejection decision

All outputs are stored under the artifacts/ directory.

---
### Key MLOps Takeaway
MLOps pipelines are about orchestrating reliable, reproducible steps — not about writing complex models.