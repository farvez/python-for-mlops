## Day 4 – Feature Preparation & Dataset Splitting (MLOps Style)

### Objective
Build a reproducible dataset preparation pipeline by transforming validated data into features and creating deterministic train/validation splits.

---

### What I Practiced
- Feature preparation from validated raw data
- Explicit, traceable feature logic
- Deterministic train/validation splitting using a fixed random seed
- Writing dataset artifacts as CSV files
- Building a multi-step dataset pipeline

---

### Why This Matters in MLOps
- Feature preparation must be **transparent and reproducible**
- Dataset splits must be **deterministic** for CI/CD and audits
- Training jobs rely on **versioned dataset artifacts**
- Pipelines must produce the same outputs given the same inputs

---

### Folder Structure
```text
day04_feature_pipeline/
│
├── data/
│ └── sample.csv
│
├── artifacts/
│ ├── train.csv
│ └── val.csv
│
├── data_loader.py
├── validator.py
├── feature_engineering.py
├── splitter.py
├── artifact_writer.py
├── dataset_pipeline.py
└── README.md

---

---

### Pipeline Flow
1. Load raw CSV data
2. Validate schema and data quality
3. Prepare features
4. Split dataset into train and validation sets
5. Write dataset artifacts

---

### How to Run
```bash
python dataset_pipeline.py

---
Expected output:
artifacts/train.csv
artifacts/val.csv