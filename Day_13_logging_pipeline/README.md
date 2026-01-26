## Day 13 – Logging & Observability in ML Pipelines (MLOps Style)

### Objective
Introduce **structured logging** into an ML pipeline to make execution observable, debuggable, and production-ready.

This day focuses on **visibility and traceability**, not model performance.

---

### What I Practiced
- Replacing `print()` statements with structured logging
- Adding logs at each pipeline stage
- Using log levels (INFO, ERROR) appropriately
- Capturing failure information through logs
- Making pipeline execution traceable end-to-end

---

### ML / MLOps Concepts Covered
- **Logging vs print:** Logs are structured, timestamped, and searchable
- **Observability:** Ability to understand what happened inside a system
- **Log levels:** INFO for normal flow, ERROR for failures
- **Operational visibility:** Logs as the first tool for debugging production issues

---

### Why This Matters in MLOps
- In production, ML pipelines run unattended
- When failures occur, logs are the primary source of truth
- Metrics explain *performance*, logs explain *behavior*
- Centralized logging enables monitoring and alerting

---

### Folder Structure
```text

day13_logging_pipeline/
│
├── data/
│ └── dataset.csv
│
├── artifacts/
│ ├── metrics.json # created on success
│ └── failure.txt # created on failure
│
├── data_loader.py
├── splitter.py
├── trainer.py
├── evaluator.py
├── validator.py
├── logger.py
├── pipeline.py
└── README.md
```

---

### Pipeline Flow
1. Initialize centralized logger
2. Log pipeline start
3. Log each major pipeline stage:
   - Data loading
   - Data splitting
   - Model training
   - Evaluation
   - Validation
4. Log success or failure outcome
5. Capture failure details when errors occur

---

### How to Run
```bash
python pipeline.py
```
---

## Example Log Output
```text
2026-01-26 21:10:12 | INFO | Pipeline started
2026-01-26 21:10:12 | INFO | Loading data
2026-01-26 21:10:12 | INFO | Training model
2026-01-26 21:10:12 | ERROR | Pipeline failed: Validation accuracy 0.65 is below threshold 0.7
```
---

## Pipeline Outcomes
Successful Run

* Logs show full execution flow

* artifacts/metrics.json is created

Failed Run

* Error is logged with context

* artifacts/failure.txt is created

* Pipeline exits immediately (fail-fast)

## Key MLOps Takeaway

Metrics tell you how good a model is.
Logs tell you what actually happened.