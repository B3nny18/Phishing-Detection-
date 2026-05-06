# Phishing Detection Using Machine Learning
**CSE 4089 - AI for Cybersecurity**
**Team: Benjamin Muniz, Peter Wilson, Theryn Kee**

## AI Use Disclaimer
Dr. Shin confirmed that we could use the GitHub Copilot Tab Autocomplete feature 
offered in VSCode. He said that we simply needed to mention that it was used as citation.
- Peter: used this feature on features.py on functions sender_domain_mismatch, 
  has_spf_fail, and timestamp_anomaly. {Side note I put this in my README but it 
  got lost in the branch merge so I rewrote it here again}

## Project Overview
This project develops and evaluates a machine learning-based phishing detection 
system using three supervised classification algorithms (Random Forest, XGBoost, 
and Decision Tree) across two data modalities: raw email text and structured URL 
features. Email-based detection uses TF-IDF vectorization on a combined dataset of 
99,608 emails. URL-based detection uses 50 engineered features from the PhiUSIIL 
dataset across 234,987 samples. Four experiments were conducted evaluating feature 
set contribution, model comparison, and TF-IDF vocabulary size impact.

**Final Results:**
- Email Dataset — Random Forest: 98.74% accuracy, 98.72% F1-score
- URL Dataset — All models: 100% accuracy 

## Requirements
- Anaconda (https://www.anaconda.com/download)
- VS Code with the Jupyter extension, or Jupyter through your browser
- A free Kaggle account to download datasets (https://www.kaggle.com)

## Setup
1. Clone the repo:
   git clone https://github.com/yourusername/phishing-detection.git

2. Install packages:
   pip install scikit-learn xgboost pandas numpy beautifulsoup4 python-whois 
   tldextract matplotlib seaborn imbalanced-learn shap joblib jupyter ipykernel

3. Download datasets (see Datasets section) and place in data/raw/
   DO NOT commit datasets to GitHub — they are already in .gitignore

## Project Structure
"
phishing-detection/
│
├── data/
│   ├── raw/              ← place downloaded datasets here
│   └── processed/        ← auto-generated cleaned data
│
├── notebooks/
│   ├── 01_eda.ipynb           ← exploratory data analysis
│   ├── 02_preprocessing.ipynb ← data cleaning and preprocessing
│   ├── 03_url_model.ipynb     ← URL dataset model training (RF, XGBoost, DT)
│   ├── 03_email_models.ipynb  ← email dataset model training (TF-IDF)
│   ├── 04_experiment1.ipynb   ← feature set comparison (URL-only, content-only, etc.)
│   ├── 04_experiment3.ipynb   ← email model comparison
│   ├── 04_experiment4.ipynb   ← TF-IDF vocabulary size analysis
│   └── 05_experiment2.ipynb   ← URL model comparison with ROC curves
│
├── src/
│   ├── init.py       ← required for imports, do not modify
│   ├── features.py       ← feature extraction functions
│   ├── models.py         ← training and evaluation functions
│   └── utils.py          ← shared helpers (plotting, data loading)
│
├── results/
│   ├── figures/          ← saved confusion matrices, ROC curves, and charts
│   ├── metrics.csv               ← URL model performance results
│   ├── email_metrics.csv         ← email model performance results
│   ├── experiment1_results.csv   ← feature set comparison results
│   ├── experiment3_results.csv   ← email model comparison results
│   └── experiment4_results.csv   ← TF-IDF vocabulary size results
│
├── .gitignore
└── README.md
"
## Datasets
Download and place in data/raw/ before running any notebooks.

- Phishing Email Dataset (Kaggle - Naser Alam)
  https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

- PhiUSIIL Phishing URL Dataset (UCI)
  https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

- Phishing Email Detection (Kaggle - Cyber Cop)
  https://www.kaggle.com/datasets/subhajournal/phishingemails

## Models
Random Forest, XGBoost, Decision Tree

## Results Summary

### Email Dataset (TF-IDF, 5000 features, 99,608 emails)
| Model         | Accuracy | Precision | Recall | F1     | AUC    |
|---------------|----------|-----------|--------|--------|--------|
| Random Forest | 98.75%   | 98.82%    | 98.65% | 98.74% | 98.75% |
| XGBoost       | 97.85%   | 96.82%    | 98.92% | 97.86% | 97.86% |
| Decision Tree | 96.63%   | 96.68%    | 96.53% | 96.60% | 96.63% |

### URL Dataset (50 engineered features, 234,987 URLs)
| Model         | Accuracy | Precision | Recall | F1     | AUC    |
|---------------|----------|-----------|--------|--------|--------|
| Random Forest | 100%     | 100%      | 100%   | 100%   | 100%   |
| XGBoost       | 100%     | 100%      | 100%   | 100%   | 100%   |
| Decision Tree | 100%     | 100%      | 100%   | 100%   | 100%   |

Note: Perfect URL scores are likely attributable to the highly discriminative 
engineered features in the PhiUSIIL dataset. See the project report for a full 
discussion of this result.


