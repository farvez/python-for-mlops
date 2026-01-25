## Day 12 – Failure Handling & Robust Pipelines (MLOps Style)

### Objective
Build a **fail-fast, production-safe ML pipeline** that stops execution when quality conditions are not met and records meaningful failure information.

This day focuses on **robustness**, not accuracy.

---

### What I Practiced
- Introducing quality gates in ML pipelines
- Failing pipelines intentionally when conditions are violated
- Preventing silent or partial pipeline success
- Capturing failure reasons as artifacts
- Differentiating between successful and failed pipeline runs

---

### ML / MLOps Concepts Covered
- **Fail-fast pipelines:** Stop execution immediately on invalid conditions
- **Quality gates:** Rules that decide whether a pipeline may proceed
- **Silent failure:** A dangerous situation where pipelines appear successful but produce invalid outputs
- **Failure artifacts:** Files that record why a pipeline failed

---

### Why This Matters in MLOps
- Production ML systems must not deploy bad models
- Pipelines should never hide failures
- Clear failure reasons reduce debugging time
- MLOps systems prioritize correctness over completion

---

### Folder Structure
```text
day12_failure_handling_pipeline/
│
├── data/
│ └── dataset.csv
│
├── artifacts/
│ ├── metrics.json # created only on success
│ └── failure.txt # created only on failure
│
├── data_loader.py
├── validator.py
├── splitter.py
├── trainer.py
├── evaluator.py
├── pipeline.py
└── README.md

```

---

### Pipeline Flow
1. Load dataset
2. Split data into training and validation sets
3. Train model
4. Evaluate validation metrics
5. Apply quality gate on validation accuracy
6. Write metrics if successful
7. Capture failure reason and exit if unsuccessful

---

### How to Run
```bash
python pipeline.py
```

### Pipeline Outcomes

Successful Run
* artifacts/metrics.json is created

* Pipeline exits normally

Failed Run

* artifacts/failure.txt is created

* Pipeline exits with error code

* No misleading metrics are written

## Example failure.txt:

```text

Validation accuracy 0.65 is below threshold 0.7
```

### Key MLOps Takeaway

A pipeline that fails loudly is safer than a pipeline that succeeds silently.