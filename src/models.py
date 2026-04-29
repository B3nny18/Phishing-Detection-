from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix)
import joblib
import time

def train_and_evaluate(model, model_name, X_train, y_train, X_val, y_val):
    # Train a model and return its performance metrics
    model.fit(X_train, y_train)
    
    start = time.time()
    y_pred = model.predict(X_val)
    inference_ms = (time.time() - start) / len(X_val) * 1000

    metrics = {
        'model': model_name,
        'accuracy': accuracy_score(y_val, y_pred),
        'precision': precision_score(y_val, y_pred),
        'recall': recall_score(y_val, y_pred),
        'f1': f1_score(y_val, y_pred),
        'inference_ms': round(inference_ms, 4)
    }

    joblib.dump(model, f'results/{model_name}.pkl')
    return metrics, confusion_matrix(y_val, y_pred)
