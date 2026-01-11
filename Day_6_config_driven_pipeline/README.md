## Day 6 – Config-Driven Training Pipelines (MLOps Style)

### Objective
Convert a hard-coded training pipeline into a flexible, config-driven system that can run multiple experiments without code changes.

---

### What I Practiced
- Using YAML files for pipeline configuration
- Loading configurations dynamically in Python
- Passing config values into training and evaluation logic
- Running multiple experiments using the same codebase
- Writing experiment outputs as structured JSON artifacts

---

### Why This Matters in MLOps
- Production pipelines must be configurable, not hard-coded
- CI/CD systems pass configs, not source code
- Reproducibility depends on storing both config and metrics
- Experiment tracking starts with config + metrics pairing

---

### Folder Structure
```text
day06_config_driven_pipeline/
│
├── configs/
│ ├── experiment1.yaml
│ └── experiment2.yaml
│
├── data/
│ └── train.csv
│
├── artifacts/
│ └── experiment_outputs/
│ ├── exp_baseline.json
│ └── exp_strict.json
│
├── config_loader.py
├── trainer.py
├── metrics.py
├── training_pipeline.py
└── README.md

```


---

### Pipeline Flow
1. Load experiment configuration from YAML
2. Simulate training using config parameters
3. Evaluate metrics against config-defined thresholds
4. Write experiment output including config and metrics
5. Store results as versioned artifacts

---

### How to Run
```bash
python training_pipeline.py --config configs/experiment1.yaml
python training_pipeline.py --config configs/experiment2.yaml

```
---

Expected outputs:

JSON files under artifacts/experiment_outputs/

Each file contains config, metrics, and approval status

---

Key MLOps Takeaway
Config-driven pipelines enable scalable, reproducible experimentation without changing code.