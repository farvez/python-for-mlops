## Day 14 – End-to-End Production-Ready ML Pipeline (v1)

### Objective
Build a **single-command, production-ready ML pipeline** that integrates real model training, reproducibility, validation, logging, quality gates, and artifact generation.

This day consolidates all previous concepts into a **realistic MLOps pipeline**.

---

### Design Philosophy
- Thin pipeline entrypoint
- Modular, reusable components
- Fail-fast behavior with quality gates
- Artifact-driven outputs
- Clear separation of concerns

---

### What I Practiced
- Designing a single pipeline entrypoint for ML workflows
- Integrating real ML training using scikit-learn
- Enforcing reproducible data splits using fixed seeds
- Evaluating models on validation data only
- Applying quality gates to prevent bad models from progressing
- Capturing metrics and failures as artifacts
- Adding structured logging for observability

---

### ML / MLOps Concepts Covered
- **End-to-end pipelines:** One command executes the full workflow
- **Reproducibility:** Same inputs and seed produce the same outputs
- **Validation metrics:** Trustworthy evaluation on unseen data
- **Quality gates:** Metric-based approval or rejection
- **Fail-fast behavior:** Stop execution immediately on invalid conditions
- **Observability:** Logs explain pipeline behavior and failures
- **Artifacts:** Models and metrics are persisted for traceability

---

### Why This Matters in MLOps
- Production ML systems must be reliable and auditable
- Silent failures and misleading metrics are unacceptable
- Pipelines must be safe to run in CI/CD and cloud environments
- This structure mirrors real-world MLOps systems used in industry

---

### Folder Structure
```text
day14_end_to_end_ml_pipeline_v1/
│
├── data/
│ └── dataset.csv
│
├── artifacts/
│ ├── model.pkl
│ ├── metrics.json
│ └── failure.txt
│
├── logger.py
├── data_loader.py
├── splitter.py
├── trainer.py
├── evaluator.py
├── validator.py
├── pipeline.py # single production entrypoint
└── README.md
```
---

### Pipeline Flow
1. Load dataset
2. Split data reproducibly (fixed seed)
3. Train a real ML model
4. Evaluate model on validation data
5. Apply quality gate on validation accuracy
6. Write model and metrics artifacts on success
7. Capture failure reason and exit on failure

---

### How to Run
Install dependencies (once):
```bash
pip install scikit-learn joblib
```
## Run the pipeline:
```bash
python pipeline.py
```
---

## Pipeline Outcomes

Successful Run
* artifacts/model.pkl is created

* artifacts/metrics.json is created

* Logs show successful completion

Failed Run
* artifacts/failure.txt is created

* No misleading model or metrics are produced

* Logs clearly describe the failure
---

### Key MLOps Takeaway

A production ML pipeline must be reproducible, observable, and safe — correctness matters more than completion.