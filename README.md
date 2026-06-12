# ML Foundations — Phase 1

A personal learning project documenting my journey into Machine Learning from the ground up. 
In IT (RPA, full-stack development, automation) but zero prior experience with gradient boosting, model explainability, or MLOps — so I built this to fix that.

---

## What this repo is

This is not a tutorial I copied. It is a structured, day-by-day curriculum I am working through myself — concept by concept, 
one small task at a time — building toward production-grade ML systems I can actually deploy for real clients.

Every file here represents something I personally ran, broke, fixed, and understood before moving on.

---

## Why I built this

I work in business process automation and have spent years automating repetitive tasks for enterprise clients. 
The next logical step was moving beyond rule-based automation into systems that *learn* — models that get better 
with data instead of needing manual rule updates every time something changes.

The use cases I care about most are Philippine government and business applications: barangay health screening, 
document classification, household assistance targeting, permit processing. That context shows up throughout this project.

---

## What is covered

### Week 1 — Core Concepts (no code)
Before touching any library, I made sure the fundamentals were solid:

- The difference between supervised, unsupervised, and reinforcement learning
- How a model actually learns — loss functions, gradient descent, the training loop
- Features, labels, training data, predictions — the vocabulary of every ML project
- Decision trees — how they split data, what root/leaf nodes are, how paths work
- Overfitting vs underfitting — why a 99% training score can mean your model is useless

### Week 2 — Hands-on with Real Data
- Environment setup — isolated virtual environment, all Phase 1 libraries installed
- Exploratory Data Analysis on the Pima Indians Diabetes Dataset
- Loading, inspecting, and questioning data before modeling

---

## Dataset

**Pima Indians Diabetes Dataset**  
768 patient records, 8 health features, binary outcome (diabetic or not).  
Source: [Jason Brownlee's public dataset mirror](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv)

I chose this dataset because it maps directly to the kind of barangay health screening tools I want to build — small, real, and messy enough to be educational.

---

## Tech stack

```
Python 3.x
pandas          — data loading and manipulation
numpy           — numerical operations
matplotlib      — basic plotting
seaborn         — statistical visualizations
scikit-learn    — pipelines, metrics, train/test split
xgboost         — gradient boosting models
lightgbm        — faster gradient boosting alternative
shap            — model explainability
optuna          — automated hyperparameter tuning
mlflow          — experiment tracking
streamlit       — interactive web app demos
polars          — fast data processing for larger datasets
```

---

## How to run this locally

```bash
# Clone the repo
git clone https://github.com/tristanSilva/ml-foundations.git
cd ml-foundations

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install xgboost lightgbm scikit-learn pandas numpy matplotlib seaborn mlflow streamlit shap optuna polars

# Run Day 7 EDA script
python day7_eda.py
```

---

## Folder structure

```
ml-foundations/
│
├── day7_eda.py          — Exploratory data analysis, first look at the dataset
├── README.md            — This file
└── requirements.txt     — All dependencies (coming soon)
```

This structure grows week by week. By the end of Phase 1 (8 weeks), this repo will contain a fully connected ML system: data pipeline → model training → experiment tracking → explainability dashboard → API → Docker deployment.

---

## Roadmap

- [x] Week 1 — ML fundamentals (concepts)
- [x] Week 2 — EDA and environment setup
- [ ] Week 3 — XGBoost and LightGBM training
- [ ] Week 4 — Evaluation metrics and scikit-learn Pipelines
- [ ] Week 5 — Optuna tuning and Polars data pipeline
- [ ] Week 6 — SHAP explainability
- [ ] Week 7 — Streamlit dashboard and MLflow tracking
- [ ] Week 8 — Capstone: full end-to-end ML system in Docker

---

## Background

Currently I am working as a Business Process Automation Developer in the Philippines, transitioning into AI Automation Engineering. 
My background is in Blue Prism RPA, NestJS, FastAPI, and React Native — mostly enterprise and LGU-facing systems.

This ML curriculum is one part of a larger effort to build AI-powered tools for Philippine government and business clients — starting with the fundamentals, done properly.

---

## License

MIT — use it, fork it, learn from it.
