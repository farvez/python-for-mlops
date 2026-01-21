## Day 10 – Experiment Tracking Mindset (Before MLflow)

### Objective
Understand what an **experiment** is in machine learning and why experiment tracking is essential in MLOps, by manually running and storing multiple experiment runs.

This day intentionally recreates the **pain that tools like MLflow solve**.

---

### What I Practiced
- Running the same ML pipeline multiple times
- Changing only one parameter (random seed)
- Capturing metrics for each run
- Storing experiment results as structured artifacts
- Comparing multiple runs manually

---

### ML / MLOps Concepts Covered
- **Experiment:** One execution of a pipeline with a specific configuration
- **Run:** A single attempt within an experiment
- **Reproducibility:** Ability to repeat results using the same setup
- **Experiment tracking:** Recording parameters and metrics for comparison

---

### Why This Matters in MLOps
- Real ML systems involve **many experiments**, not one-off runs
- Without tracking, results become unmanageable and unreliable
- MLOps platforms require traceability of:
  - parameters
  - metrics
  - outcomes
- Understanding this pain makes MLflow intuitive, not magical

---

### Folder Structure
```text
day10_experiment_tracking_basics/
│
├── data/
│ └── dataset.csv
│
├── artifacts/
│ └── experiments/
│ ├── run_1.json
│ ├── run_2.json
│ └── run_3.json
│
├── data_loader.py
├── splitter.py
├── trainer.py
├── evaluator.py
├── experiment_runner.py
└── README.md
```


---

### Pipeline Flow
1. Load dataset
2. Split data using a specific random seed
3. Train a model
4. Evaluate on validation data
5. Store metrics for each run
6. Repeat for multiple seeds

Each execution represents a **separate experiment run**.

---

### How to Run
Install dependencies if needed:
```bash
pip install scikit-learn joblib
Run the experiment runner:
```
```bash
python experiment_runner.py
```
---

### Pipeline Outputs
After execution, multiple experiment result files are created:

* artifacts/experiments/run_1.json

* artifacts/experiments/run_2.json

* artifacts/experiments/run_3.json

Each file contains:

* run ID

* parameters (seed)

* validation metrics
---

### Key MLOps Takeaway
When experiments increase, manual tracking breaks down.
This is exactly why experiment tracking tools like MLflow are required.