## Day 5 – Metrics, Training Simulation & Experiment Outputs (MLOps Style)

### Objective
Simulate a training job and generate experiment-style outputs by computing metrics, making promotion decisions, and storing results as artifacts.

---

### What I Practiced
- Simulating a training step without ML frameworks
- Separating training logic from evaluation logic
- Calculating metrics and promotion status
- Writing metrics as JSON artifacts
- Producing pipeline decision outputs

---

### Why This Matters in MLOps
- Training jobs run as isolated pipeline steps
- Metrics determine whether a model is promoted or rejected
- Experiment outputs must be stored as artifacts for traceability
- Separation of concerns improves pipeline maintainability

---

### Folder Structure

```text
day05_metrics_pipeline/
│
├── data/
│ └── train.csv
│
├── artifacts/
│ ├── metrics.json
│ └── status.txt
│
├── trainer.py
├── metrics.py
├── training_pipeline.py
└── README.md

```


---

### Pipeline Flow
1. Simulate a training job
2. Generate raw training metrics
3. Evaluate metrics against a threshold
4. Write metrics and status artifacts
5. Log training outcome

---

### How to Run
```bash
python training_pipeline.py

```
---

### Expected outputs:

artifacts/metrics.json

artifacts/status.txt
---

### Key MLOps Takeaway
Metrics and experiment outputs are first-class citizens in MLOps pipelines.