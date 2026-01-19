## Day 9 – Train / Validation Split & Trustworthy Metrics (MLOps Style)

### Objective
Introduce proper model evaluation by separating training data from validation data and generating **trustworthy metrics** that reflect real model performance.

This day focuses on **correct ML evaluation practices**, which are critical in MLOps.

---

### What I Practiced
- Splitting data into training and validation sets
- Training a model only on training data
- Evaluating the model only on validation data
- Generating realistic evaluation metrics
- Understanding why evaluation on training data is misleading

---

### ML Concepts Covered (Intuitive)
- **Train data:** Used to teach the model patterns
- **Validation data:** Used to test how well the model generalizes
- **Overfitting:** Model performs well on training data but poorly on unseen data
- **Validation accuracy:** Metric that reflects real-world performance

---

### Why This Matters in MLOps
- Models evaluated on training data give **fake confidence**
- Production systems rely on validation metrics to accept or reject models
- MLOps pipelines enforce separation of training and evaluation
- Poor evaluation leads to bad models reaching production

---

### Folder Structure
```text
day09_train_val_ml_pipeline/
│
├── data/
│ └── dataset.csv
│
├── artifacts/
│ ├── model.pkl
│ └── metrics.json
│
├── data_loader.py
├── splitter.py
├── trainer.py
├── evaluator.py
├── pipeline.py
└── README.md
```


---

### Pipeline Flow
1. Load dataset from CSV
2. Split data into training and validation sets
3. Train the model on training data only
4. Evaluate the model on validation data only
5. Store trained model and validation metrics as artifacts

---

### How to Run
Install dependencies (if not already installed):
```bash
pip install scikit-learn joblib
```
### Run the pipeline:
```bash
python pipeline.py
```
---

### Pipeline Outputs

After execution, the following artifacts are generated:

artifacts/model.pkl – trained machine learning model

artifacts/metrics.json – validation metrics

Example metrics.json:

```json

{
  "validation_accuracy": 0.8
}
```
---

###Key MLOps Takeaway

In MLOps, validation metrics matter more than training metrics.
A model is only as good as its performance on unseen data.