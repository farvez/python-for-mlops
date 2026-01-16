## Day 8 – Real ML Training with scikit-learn (MLOps Perspective)

### Objective
Introduce a real machine learning model into the existing pipeline mindset and understand how model training, evaluation, and artifacts fit into MLOps systems.

This day focuses on **conceptual clarity + hands-on ML**, without heavy math.

---

### What I Practiced
- Understanding what a machine learning model is in practical terms
- Loading structured data for ML training
- Training a real ML model using scikit-learn
- Evaluating the model using accuracy
- Storing models and metrics as pipeline artifacts

---

### ML Concepts Covered (Beginner-Friendly)
- **Features (X):** Input variables used for prediction
- **Label (y):** Target variable to predict
- **Training:** Fitting a model on data
- **Evaluation:** Measuring how well the model performs
- **Accuracy:** Percentage of correct predictions

---

### Why This Matters in MLOps
- Models are treated as **artifacts**, not temporary objects
- Training is just one step in a larger pipeline
- Metrics decide whether a model is usable
- Reproducible training pipelines are required in production

---

### Folder Structure

```text
day08_real_ml_pipeline/
│
├── data/
│ └── dataset.csv
│
├── artifacts/
│ ├── model.pkl
│ └── metrics.json
│
├── data_loader.py
├── trainer.py
├── evaluator.py
├── pipeline.py
└── README.md

```
---

### Pipeline Flow
1. Load dataset from CSV
2. Separate features (X) and labels (y)
3. Train a Logistic Regression model
4. Evaluate the model using accuracy
5. Save the trained model as an artifact
6. Save evaluation metrics as JSON

---

### How to Run
Install dependencies (once):
```bash
pip install scikit-learn joblib

```
### Run the pipeline:
```bash
python pipeline.py
```
---
### Pipeline Outputs
After running the pipeline, the following artifacts are created:

artifacts/model.pkl – trained ML model

artifacts/metrics.json – evaluation metrics

---

### Key MLOps Takeaway

In MLOps, models and metrics are first-class artifacts.
Training is important, but evaluation and reproducibility matter more.