



# Bugs
- Import of xgboost (5/1/26)
    - ModuleNotFound
    - Solved by changeing the selected kernal to the my_env (5/1/26)
- Import of src.models and src.utils (5/1/26)
    - ModuleNotFoundError: No module named 'src'
    - 


----------------------------------------------------------------------------------


## Peter Wilson — Header/Metadata Features + Model Training + Evaluation

### Responsibilities
- Implementing all header and metadata feature extraction functions
- Training, tuning, and evaluating all four ML models
- Running both experiments and saving all results

### Features You Are Implementing
Add all of these to src/features.py under the Header Features section:

- sender_domain_mismatch: compares the From: domain against domains
  found in the email body — returns 0 or 1

- has_spf_fail: checks email headers for SPF authentication failure
  — returns 0 or 1

- timestamp_anomaly: compares the Date: header against the Received:
  timestamp — returns 1 if difference exceeds 24 hours


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
    - sender_domain_mismatch 
    - has_spf_fail
    - timestamp_anomaly **(DONE)**

2. Build the full train_and_evaluate() function in src/models.py
   that handles training, timing inference, computing all metrics,
   saving the model with joblib, and returning results

3. Run hyperparameter tuning with GridSearchCV for all four models

4. Generate confusion matrices and ROC curves for all models and
   save them to results/figures/

5. Save all metrics to results/metrics.csv

6. Run final evaluation on the test set with the best model only