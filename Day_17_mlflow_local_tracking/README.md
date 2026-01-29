## Day 17 – MLflow Local Experiment Tracking (Hands-on)

### Objective
Introduce **MLflow for local experiment tracking** and replace manual experiment logging with an industry-standard tool.

This day focuses on **tracking parameters, metrics, and models automatically** and visualizing results using the MLflow UI.

---

### What I Practiced
- Installing and configuring MLflow locally
- Logging ML experiments using MLflow
- Tracking parameters, metrics, and models
- Running multiple experiments with the same pipeline
- Visualizing experiment results using the MLflow UI

---

### ML / MLOps Concepts Covered
- **Experiment:** A collection of related ML runs
- **Run:** One execution of the ML pipeline
- **Parameters:** Configuration values (e.g., seed, model type)
- **Metrics:** Evaluation results (e.g., validation accuracy)
- **Artifacts:** Output files such as trained models
- **Tracking URI:** Location where MLflow stores experiment data

---

### Folder Structure
```text
day17_mlflow_local_tracking/
│
├── data/
│ └── dataset.csv
│
├── mlruns/ # created automatically by MLflow (ignored in git)
│
├── train.py
├── pipeline.py
└── README.md
```


---

### How the Pipeline Works
1. Load dataset
2. Split data reproducibly using a fixed seed
3. Train a machine learning model
4. Evaluate the model on validation data
5. Log parameters, metrics, and model using MLflow
6. View results in the MLflow UI

---

### How to Run

Install dependencies (once):
```bash
pip install mlflow scikit-learn joblib
```

Run the pipeline:
```bash
python pipeline.py
```

Start the MLflow UI (from the same directory):
```bash
mlflow ui
```
Open in browser:
```text
http://127.0.0.1:5000

```
---

### Expected Outcome

* Each pipeline execution creates a new MLflow run

* Parameters, metrics, and models are visible in the MLflow UI

* No manual JSON or model file management is required
---

### Key MLOps Takeaway

MLflow automates experiment tracking and makes ML pipelines reproducible, comparable, and auditable.