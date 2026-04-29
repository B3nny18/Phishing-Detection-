# Team Task Breakdown

## Benjamin Muniz — URL Features + Repo Setup + Preprocessing Pipeline

### Responsibilities
- Leading the data preprocessing pipeline
- Implementing all URL-based feature extraction functions

### Files You Own
- src/features.py (URL Features section)
- notebooks/01_eda.ipynb
- notebooks/02_preprocessing.ipynb

### Files You Will Read But Not Own
- src/models.py (read to understand how your features feed into training)
- data/raw/ (all datasets)

### Datasets You Work With
- PhiUSIIL Phishing URL Dataset (UCI) — primary URL dataset
  https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset
- Phishing Email Dataset (Kaggle - Naser Alam) — contains URLs embedded
  in emails
  https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

### Features You Are Implementing
Add all of these to src/features.py under the URL Features section:

- has_ip_url: detects if the URL contains a raw IP address instead of
  a domain name (e.g. http://192.168.1.1/login) — returns 0 or 1
- has_fresh_domain: checks WHOIS data to see if domain was registered
  less than 60 days ago — returns 0 or 1
- has_nonmatching_url: checks if the visible link text and the actual
  href destination are different — returns 0 or 1
- num_links: counts total number of anchor tags in the email — returns int
- num_domains: counts unique domains extracted from all URLs — returns int
- max_dots: counts the maximum number of dots in any single URL
  (lots of dots = suspicious subdomain stacking) — returns int
- has_url_shortener: detects known URL shortening services
  (bit.ly, tinyurl, goo.gl, t.co, ow.ly) — returns 0 or 1

### Your Goals
1. Load all four datasets and confirm they open correctly with pandas
2. Perform EDA on each dataset in 01_eda.ipynb:
   - Check shape, dtypes, null values, class balance
   - Document findings with markdown cells in the notebook
   - Flag any datasets with significant class imbalance (>60/40 split)
3. Clean and standardize all datasets in 02_preprocessing.ipynb:
   - Drop duplicates and rows with excessive nulls
   - Standardize label column to 0 (legitimate) and 1 (phishing)
   - Save the cleaned combined dataset to data/processed/features.csv
4. Implement and test all 7 URL feature functions in src/features.py
5. Apply your feature functions to the dataset and add columns to the
   feature matrix

### Desired Results / Benchmarks
- EDA notebook fully documents all 4 datasets before any cleaning
- Zero null values in data/processed/ after preprocessing
- 70/15/15 train/validation/test split saved and confirmed balanced
- All 7 URL feature functions tested individually with at least one
  phishing URL and one legitimate URL as a sanity check
- URL-only features achieve at least 85% accuracy in Experiment 1
  when trained on Random Forest alone (baseline expectation)

### Deliverables
- 01_eda.ipynb complete with findings documented
- 02_preprocessing.ipynb complete with cleaned data saved
- URL Features section of src/features.py complete and tested
- data/processed/X_train.csv, X_val.csv, X_test.csv, y_train.csv,
  y_val.csv, y_test.csv saved and committed (these are processed
  data so they can go in Git unlike raw datasets)

---

## Theryn Kee — Email Content Features

### Responsibilities
- Implementing all email content-based feature extraction functions
- Analyzing the email body text and HTML structure of emails

### Files You Own
- src/features.py (Content Features section)
- notebooks/03_features.ipynb (content features portion)

### Files You Will Read But Not Own
- notebooks/02_preprocessing.ipynb (to understand cleaned data format)
- data/processed/features.csv (your input data)

### Datasets You Work With
- Phishing Email Dataset (Kaggle - Naser Alam) — primary email body dataset
  https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset
- Phishing Email Detection (Kaggle - Cyber Cop) — additional email text
  https://www.kaggle.com/datasets/subhajournal/phishingemails

### Features You Are Implementing
Add all of these to src/features.py under the Content Features section:

- is_html: checks email MIME type or body for HTML tags — returns 0 or 1
- has_javascript: detects <script> tags in email body — returns 0 or 1
- has_form: detects <form> tags (used to steal credentials) — returns 0 or 1
- num_suspicious_keywords: counts occurrences of high-risk words:
  "verify", "urgent", "suspended", "confirm", "update", "account",
  "click here", "limited time" — returns int
- link_text_ratio: ratio of characters inside anchor tags to total
  body text length — returns float between 0 and 1
- has_nonmodal_here_link: detects deceptive "click here" style links
  where the text says one thing but href goes somewhere else
  — returns 0 or 1

### Your Goals
1. Familiarize yourself with the email body format in both datasets
   (some will be raw text, some will be HTML — handle both cases)
2. Implement all 6 content feature functions in src/features.py
3. Test each function on at least 3 sample emails (mix of phishing
   and legitimate) to confirm they return sensible values
4. Apply all functions to the full dataset and add as new columns

### Desired Results / Benchmarks
- All functions handle edge cases gracefully:
  empty strings, None values, non-HTML emails, and malformed HTML
  should never cause a crash — use try/except where needed
- Content-only features achieve at least 80% accuracy in Experiment 1
  when trained on Random Forest alone
- num_suspicious_keywords should show a clear difference between
  phishing emails (expected average 3-5 keywords) and legitimate
  emails (expected average 0-1 keywords) — verify this in EDA

### Deliverables
- Content Features section of src/features.py complete and tested
- Short markdown cell in 03_features.ipynb showing sample output
  of each function on one phishing and one legitimate email

---

## Peter Wilson — Header/Metadata Features + Model Training + Evaluation

### Responsibilities
- Implementing all header and metadata feature extraction functions
- Training, tuning, and evaluating all four ML models
- Running both experiments and saving all results

### Files You Own
- src/features.py (Header Features section)
- src/models.py (full file)
- notebooks/03_models.ipynb
- notebooks/04_experiment1.ipynb
- notebooks/05_experiment2.ipynb

### Files You Will Read But Not Own
- src/utils.py (use the load_splits() function to load data)
- data/processed/ (your input data)

### Datasets You Work With
- Phishing Email Curated Datasets (Zenodo - Champa et al.)
  https://zenodo.org/records/8339691
  This dataset contains the richest header and metadata information
  including sender details, timestamps, and authentication fields

### Features You Are Implementing
Add all of these to src/features.py under the Header Features section:

- sender_domain_mismatch: compares the From: domain against domains
  found in the email body — returns 0 or 1
- has_spf_fail: checks email headers for SPF authentication failure
  — returns 0 or 1
- timestamp_anomaly: compares the Date: header against the Received:
  timestamp — returns 1 if difference exceeds 24 hours

### Models You Are Training
All four models in notebooks/03_models.ipynb using src/models.py:

- Random Forest (expected 94-96% accuracy)
- XGBoost (expected 94-96% accuracy)
- SVM (expected 92-95% accuracy)
- Decision Tree (expected 88-92% accuracy)

### Experiments You Are Running

Experiment 1 (04_experiment1.ipynb) — Feature Set Comparison:
  Train Random Forest three separate times:
  - Run 1: URL-only features (Benjamin's features)
  - Run 2: Content-only features (Theryn's features)
  - Run 3: Header-only features (your features)
  - Run 4: All features combined
  Goal: show which feature category contributes most to accuracy

Experiment 2 (05_experiment2.ipynb) — Model Comparison:
  Train all four models on the full combined feature set
  and compare them side by side using identical data splits
  Goal: identify the best performing model overall

### Your Goals
1. Implement all 3 header feature functions in src/features.py
2. Build the full train_and_evaluate() function in src/models.py
   that handles training, timing inference, computing all metrics,
   saving the model with joblib, and returning results
3. Run hyperparameter tuning with GridSearchCV for all four models
4. Generate confusion matrices and ROC curves for all models and
   save them to results/figures/
5. Save all metrics to results/metrics.csv
6. Run final evaluation on the test set with the best model only

### Desired Results / Benchmarks
- Minimum: at least one model hits >= 93% accuracy
- Target: at least one model hits >= 95% accuracy
- Stretch: at least one model hits >= 96% accuracy
- False positive rate <= 1% (legitimate email flagged as phishing)
- Inference time < 15ms per email for all models
- All confusion matrices and ROC curves saved to results/figures/
- results/metrics.csv contains accuracy, precision, recall, F1,
  AUC, and inference time for every model

### Deliverables
- Header Features section of src/features.py complete and tested
- src/models.py complete with train_and_evaluate() function
- 03_models.ipynb complete with all four models trained and tuned
- 04_experiment1.ipynb complete with feature comparison results
- 05_experiment2.ipynb complete with model comparison results
- results/metrics.csv with all final numbers
- results/figures/ with all confusion matrices and ROC curves

---

## Shared Responsibilities (Everyone)

### Git Rules
- Always pull before starting a session: git pull origin main
- Never push directly to main — always use a branch and open
  a pull request
- Write clear commit messages describing what you did
- Commit at the end of every work session even if not finished

### Code Standards
- Every function in src/ must have a docstring explaining what it
  does, what it takes as input, and what it returns
- All feature functions must return either an int (0 or 1) or a
  float — never a string or boolean
- Handle None and empty string inputs without crashing
- Use random_state=489 everywhere randomness is involved so results
  are reproducible across all three machines

