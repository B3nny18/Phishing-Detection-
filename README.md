# Phishing Email Detection

## AI use disclaimer
Dr Shin confimed that we could use the Github's Copilot Tab Autocomplete feature offered in VSCode. He said that we simply needed to mention that it was used as citation.
- Peter: used this feature on features.py on functions sender_domain_mismatch, has_spf_fail, and timestamp_anomaly. {Side note I put this in my README but it got lost in the branch merge so I rewrote it here again}

## Project Overview
Machine learning model to classify emails as phishing or legitimate using supervised binary classification. The model analyzes three categories of features: URL-based features, email content-based features, and header/metadata features. Four ML algorithms are compared: Random Forest, XGBoost, SVM, and Decision Tree. The goal is to achieve at least 95% accuracy with under 15ms inference time per email.

## Requirements
- Anaconda installed (https://www.anaconda.com/download)
- VS Code with the Jupyter extension installed or through desired browser
- A Kaggle account to download datasets (https://www.kaggle.com), but an account is free

## Setup
1. Clone the repo:
   git clone https://github.com/yourusername/phishing-detection.git

2. Install packages:
   pip install scikit-learn xgboost pandas numpy beautifulsoup4 python-whois tldextract matplotlib seaborn imbalanced-learn shap joblib jupyter ipykernel

3. Download datasets (see Datasets section) and place in data/raw/
   DO NOT commit datasets to GitHub because they are already in .gitignore. 

## Project Structure
```
phishing-detection/
│
├── data/
│   ├── raw/              ← place downloaded datasets here
│   └── processed/        ← auto-generated cleaned data
│
├── notebooks/
│   ├── 01_eda.ipynb           ← exploratory data analysis
│   ├── 02_preprocessing.ipynb ← cleaning and feature extraction
│   ├── 03_models.ipynb        ← training all 4 models
│   ├── 04_experiment1.ipynb   ← feature set comparison
│   └── 05_experiment2.ipynb   ← model comparison
│
├── src/
│   ├── __init__.py       ← do not touch, required for imports
│   ├── features.py       ← all feature extraction functions
│   ├── models.py         ← training and evaluation functions
│   └── utils.py          ← shared helpers (plotting, loading data)
│
├── results/
│   ├── figures/          ← saved confusion matrices and ROC curves
│   └── metrics.csv       ← model performance results
│
├── .gitignore
└── README.md
```

## Datasets
Download and place in data/raw/ before running any notebooks.

- Phishing Email Dataset (Kaggle - Naser Alam)
  https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

- PhiUSIIL Phishing URL Dataset (UCI)
  https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

- Phishing Email Detection (Kaggle - Cyber Cop)
  https://www.kaggle.com/datasets/subhajournal/phishingemails

## Models
Random Forest, XGBoost, SVM, Decision Tree

## Performance Targets
- Accuracy:  >= 95%
- Precision: >= 90%
- Recall:    >= 95%
- F1-Score:  >= 92%
- False Positive Rate: <= 1%
- Inference Time: < 15ms per email

## Team Responsibilities
- Benjamin: URL-based features, repo setup, preprocessing pipeline
- Theryn:   Email content-based features (HTML, keywords, links)
- Peter:    Header/metadata features, model training and evaluation

## Results
See results/metrics.csv
