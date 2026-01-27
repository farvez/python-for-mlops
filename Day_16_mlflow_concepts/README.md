## Day 16 – MLflow Concepts (Why It Exists, What It Replaces)

### Objective
Understand **why MLflow exists**, what problems it solves in MLOps, and how it maps directly to the manual experiment tracking pipelines built earlier.

This day is **concept-focused** and does not include implementation.

---

### What I Learned
- What an ML experiment is in production systems
- Why manual experiment tracking does not scale
- How MLflow standardizes experiment tracking
- The difference between experiments, runs, metrics, parameters, and artifacts
- How MLflow replaces custom experiment folders and JSON files

---

### What Problem MLflow Solves
Before MLflow:
- Metrics stored manually in JSON files
- No easy way to compare runs
- No centralized history
- No UI for inspection
- Ad-hoc model selection logic

With MLflow:
- Automatic run tracking
- Parameter and metric logging
- Centralized experiment history
- UI for comparison
- Structured model versioning

---

### Core MLflow Components

#### 1. Tracking
- Logs parameters (e.g., seed, thresholds)
- Logs metrics (e.g., validation accuracy)
- Logs artifacts (models, files)
- Assigns unique run IDs

#### 2. Experiments
- Groups related runs together
- Enables comparison across runs

#### 3. Model Registry
- Centralized model storage
- Versioned models
- Lifecycle stages (Staging, Production, Archived)

#### 4. Projects (Optional)
- Package ML code for reproducible execution
- Not required in the current phase

---

### Mapping Previous Work to MLflow

| Manual Pipeline Work | MLflow Equivalent |
|----------------------|-------------------|
| metrics.json         | mlflow.log_metric |
| model.pkl     | mlflow.sklearn.log_model |
| seed variable        | mlflow.log_param  |
| experiments folder   | MLflow Experiments|
| best-model logic     | Model Registry    |

---


### Key MLOps Takeaway
> MLflow does not introduce new ideas — it **automates and standardizes** experiment tracking concepts already used in MLOps pipelines.

---

### Next Steps
Day 17 will introduce **hands-on MLflow local tracking**, replacing manual experiment artifacts with MLflow runs and UI-based comparison.
