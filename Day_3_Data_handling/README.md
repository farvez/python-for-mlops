## Day 3 – Data Handling & Validation for MLOps

### Objective
Learn how real MLOps pipelines ingest data, validate quality, and fail safely before model training.

---

### What I Practiced
- Loading CSV data using Python standard libraries
- Loading JSON files for metrics/configs
- Schema validation (required fields check)
- Data quality checks (nulls, value ranges)
- Failing pipelines safely with clear error reporting
- Generating data quality artifacts

---

### Why This Matters in MLOps
- Most production ML failures happen due to **bad data**, not bad models
- MLOps engineers are responsible for **early data validation**
- Pipelines must **fail fast and safely** to prevent corrupted training
- Data quality reports are critical for debugging and auditing

---

### Folder Structure
day03_data_handling/
│
├── data/
│ └── sample.csv
│
├── artifacts/
│ └── data_quality_report.txt
│
├── data_loader.py
├── validator.py
├── data_pipeline.py
└── README.md


---

### How the Pipeline Works
1. Load raw CSV data
2. Validate schema (required columns)
3. Validate data quality (nulls, ranges)
4. Collect all validation errors
5. Write a data quality report if errors exist
6. Fail the pipeline safely

---

### How to Run
```bash
python data_pipeline.py

```
If data issues are found:

Pipeline exits with error

artifacts/data_quality_report.txt is created

If data is valid:

Pipeline completes successfully