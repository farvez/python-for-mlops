## Day 11 – Reproducibility & Random Seeds (MLOps Critical Concept)

### Objective
Ensure that machine learning experiments produce **consistent and trustworthy results** by controlling randomness using fixed seeds.

This day focuses on understanding and enforcing **reproducibility**, a core requirement in MLOps.

---

### What I Practiced
- Identifying sources of randomness in ML pipelines
- Controlling randomness using a fixed seed
- Running the same pipeline multiple times with the same seed
- Verifying that results remain identical across runs
- Demonstrating controlled variation by changing the seed

---

### ML / MLOps Concepts Covered
- **Reproducibility:** Same inputs, same code, same configuration → same results
- **Random seed:** A fixed value used to control randomness
- **Deterministic pipeline:** Pipeline that produces identical outputs when inputs and seed are unchanged
- **Controlled variability:** Expected changes when the seed is intentionally changed

---

### Why This Matters in MLOps
- Non-reproducible experiments cannot be trusted
- Teams must be able to re-run experiments and get the same results
- Debugging and comparison are impossible without reproducibility
- Production ML systems require deterministic behavior for audits and rollbacks

---

### Folder Structure

```text
day11_reproducibility_pipeline/
│
├── data/
│ └── dataset.csv
│
├── artifacts/
│ ├── run_seed_42.json
│ └── run_seed_42_repeat.json
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
1. Load dataset
2. Split data using a fixed random seed
3. Train the model
4. Evaluate on validation data
5. Store metrics as artifacts
6. Repeat the pipeline with the same seed

---

### How to Run
```bash
python pipeline.py
```

### After execution, compare:

* run_seed_42.json

* run_seed_42_repeat.json

### Both files should contain identical metrics.
---

### Key MLOps Takeaway

Reproducibility ensures that experiment results are trustworthy, comparable, and debuggable.