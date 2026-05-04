# ================================================
# src/models.py
# Purpose: Training and evaluation functions for all four ML models
# ================================================

from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score,
                             confusion_matrix, roc_auc_score)
import joblib
import time
import os

def train_and_evaluate(model, model_name, X_train, y_train, X_val, y_val):
    """Trains a model and returns performance metrics and confusion matrix.

    Args:
        model: sklearn or xgboost model instance
        model_name: string name for saving the model file
        X_train: training features dataframe
        y_train: training labels series
        X_val: validation features dataframe
        y_val: validation labels series

    Returns:
        metrics: dict containing accuracy, precision, recall,
                 f1, auc, and inference_ms
        cm: confusion matrix numpy array
    """
    # Train the model
    model.fit(X_train, y_train)

    # Measure inference time per email in milliseconds
    start = time.time()
    y_pred = model.predict(X_val)
    inference_ms = (time.time() - start) / len(X_val) * 1000

    # Compute all performance metrics
    metrics = {
        'model':        model_name,
        'accuracy':     accuracy_score(y_val, y_pred),
        'precision':    precision_score(y_val, y_pred, zero_division=0),
        'recall':       recall_score(y_val, y_pred, zero_division=0),
        'f1':           f1_score(y_val, y_pred, zero_division=0),
        'auc':          roc_auc_score(y_val, y_pred),
        'inference_ms': round(inference_ms, 4)
    }

    # Save the trained model to results/
    os.makedirs('../results', exist_ok=True)
    joblib.dump(model, f'../results/{model_name}.pkl')
    print(f"Model saved to results/{model_name}.pkl")

    return metrics, confusion_matrix(y_val, y_pred)