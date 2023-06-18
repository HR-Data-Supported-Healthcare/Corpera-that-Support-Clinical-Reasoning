import json
from sklearn.model_selection import StratifiedKFold
import numpy as np

def import_data(data_dir: str) -> dict:
    print("[importing dataset]")
    with open(data_dir, "r") as f: return json.load(f)

def generate_training_test_folds(fold_number: int, data: dict) -> tuple:
    print("[generating training test folds]")
    X = [d["text"] for d in data]
    y = [d["label"] for d in data]
    skf = StratifiedKFold(n_splits=fold_number, shuffle=True, random_state=9999)
    return skf.split(X, y)

def retrieve_training_test_data(fold: tuple, data: dict) -> tuple:
    print("[retrieving training test data]")
    training_idxs, dev_indx = fold
    X_train = []
    y_train = []
    for idx in training_idxs:
        X_train.append(data[idx]["text"])
        y_train.append(data[idx]["label"])
    X_val = []
    y_val = []
    for idx in dev_indx:
        X_val.append(data[idx]["text"])
        y_val.append(data[idx]["label"])
    return (X_train, np.array(y_train)), (X_val, np.array(y_val))
