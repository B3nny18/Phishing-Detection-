import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_splits():
    # Load all train/val/test splits at once
    X_train = pd.read_csv('../data/processed/X_train.csv')
    X_val   = pd.read_csv('../data/processed/X_val.csv')
    X_test  = pd.read_csv('../data/processed/X_test.csv')
    y_train = pd.read_csv('../data/processed/y_train.csv').squeeze()
    y_val   = pd.read_csv('../data/processed/y_val.csv').squeeze()
    y_test  = pd.read_csv('../data/processed/y_test.csv').squeeze()
    return X_train, X_val, X_test, y_train, y_val, y_test

def plot_confusion_matrix(cm, model_name):
    # Save a confusion matrix heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Legitimate', 'Phishing'],
                yticklabels=['Legitimate', 'Phishing'])
    plt.title(f'{model_name} Confusion Matrix')
    plt.tight_layout()
    plt.savefig(f'../results/figures/{model_name}_cm.png', dpi=150)
    plt.show()
