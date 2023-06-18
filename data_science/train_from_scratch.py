import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
import keras.backend as K
import csv
from .utils import generate_training_test_folds, import_data, retrieve_training_test_data

#Classes
class TrainingEpochResult:
    def __init__(self, f1: float, precision: float, recall: float, loss: float) -> None:
        self.f1 = f1
        self.precision = precision
        self.recall = recall
        self.loss = loss

class TrainingResultStreaks:
    def __init__(self, f1_streak: list[float], precision_streak: list[float], recall_streak: list[float], loss_streak: list[float]) -> None:
        self.f1_streak = f1_streak
        self.precision_streak = precision_streak
        self.recall_streak = recall_streak
        self.loss_streak = loss_streak

#Functions
def import_data_csv_to_streak(data_dir: str)-> TrainingResultStreaks:
    print("[importing csv data]")
    f1_streak = []
    p_streak = []
    r_streak = []
    l_streak = []
    with open(data_dir, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            f1_streak.append(row["f1"])
            p_streak.append(row["precision"])
            r_streak.append(row["recall"])
            l_streak.append(row["loss"])
    return TrainingResultStreaks(f1_streak, p_streak, r_streak, l_streak)

def compute_avg_training_epochs(folds_training_results: list[list[TrainingEpochResult]])-> list[TrainingEpochResult]:
    print("[computing avg]")
    epoch_amt = len(folds_training_results[0])
    fold_amt = len(folds_training_results)
    f1_sum = [0 for _ in range(len(folds_training_results[0]))]
    p_sum = [0 for _ in range(len(folds_training_results[0]))]
    r_sum = [0 for _ in range(len(folds_training_results[0]))]
    loss_sum = [0 for _ in range(len(folds_training_results[0]))]
    for res in folds_training_results:
        for epoch_indx in range(epoch_amt):
            f1_sum[epoch_indx] += res[epoch_indx].f1
            p_sum[epoch_indx] += res[epoch_indx].precision
            r_sum[epoch_indx] += res[epoch_indx].recall
            loss_sum[epoch_indx] += res[epoch_indx].loss
    f1_avg = [f1_s / fold_amt for f1_s in f1_sum]
    p_avg = [p_s / fold_amt for p_s in p_sum]
    r_avg = [r_s / fold_amt for r_s in r_sum]
    loss_avg = [loss_s / fold_amt for loss_s in loss_sum]
    return_list = []
    for i in range(epoch_amt):
        return_list.append(TrainingEpochResult(f1_avg[i], p_avg[i], r_avg[i], loss_avg[i]))
    return return_list

def export_data(data_dir: str, data: list[TrainingEpochResult], fold: int = -1) -> None:
    print("[exporting dataset]")
    with open(data_dir, 'w', newline='') as f:
        fieldnames = ['fold', 'epoch', 'f1', 'precision', 'recall', 'loss']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        row_to_write = {}
        for i, d in enumerate(data):
            row_to_write["epoch"] = i +1
            row_to_write["fold"] = fold +1
            row_to_write["f1"] = d.f1
            row_to_write["precision"] = d.precision
            row_to_write["recall"] = d.recall
            row_to_write["loss"] = d.loss
            writer.writerow(row_to_write)

def transform_tf_history_data(f1: list[float], precision: list[float], recall: list[float], loss: list[float]) -> list[TrainingEpochResult]:
    print("[transforming dataset]")
    total_epochs = len(f1)
    return_list = []
    for i in range(total_epochs):
        return_list.append(TrainingEpochResult(f1[i], precision[i], recall[i], loss[i]))
    return return_list

def transform_training_epoch_list_to_streak(data: list[TrainingEpochResult]) -> TrainingResultStreaks:
    f_streak = []
    p_streak = []
    r_streak = []
    loss_streak = []
    for d in data:
        f_streak.append(d.f1)
        p_streak.append(d.precision)
        r_streak.append(d.recall)
        loss_streak.append(d.loss)
    return TrainingResultStreaks(f_streak, p_streak, r_streak, loss_streak)

def f1_metric(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val

def plot_results(plot_title: str, metrics: TrainingResultStreaks, baseline_metrics: TrainingResultStreaks) -> None:
    fig, axs = plt.subplots(1, 2)
    fig.suptitle(plot_title, fontsize=14)
    fig.supxlabel('epoch')
    fig.supylabel('performance')    
    axs[0].plot(metrics.f1_streak, label='f1')
    axs[0].plot(metrics.precision_streak, label='precision')
    axs[0].plot(metrics.recall_streak, label='recall')
    axs[1].plot(metrics.loss_streak, label='loss')
    floats = [float(metric) for metric in baseline_metrics.f1_streak]
    if baseline_metrics is not None:
        axs[0].plot([float(metric) for metric in baseline_metrics.f1_streak], label='baseline f1', linestyle='dashdot', color="0.3")
        axs[0].plot([float(metric) for metric in baseline_metrics.precision_streak], label='baseline p', linestyle='dashed', color="0.3")
        axs[0].plot([float(metric) for metric in baseline_metrics.recall_streak], label='baseline r', linestyle='dotted', color="0.3")
        axs[1].plot([float(metric) for metric in baseline_metrics.loss_streak], label='loss', linestyle='dotted', color="0.3")
    axs[0].legend()
    axs[1].legend()
    axs[0].invert_yaxis()
    axs[1].invert_yaxis()
    #list = np.arange(0.1, 1, 0.1)
    #plt.yticks()
    axs[0].set_yticks(np.arange(0.0, 1.0, 0.1))
    #axs[1].set_yticks(list)

    #TODO: Save plot without showing
    plt.show()

def transform_dataset(X_features: list[str], y_labels: list[int]):
    X_features_one_hot = [tf.keras.preprocessing.text.one_hot(d, 40, filters='', lower=False) for d in X_features]
    X_features_one_hot_padded = tf.keras.preprocessing.sequence.pad_sequences(X_features_one_hot, maxlen=40, padding='post')
    y_labels_categorial = tf.keras.utils.to_categorical(y_labels, num_classes=3)
    return X_features_one_hot_padded, y_labels_categorial

#Constants
#Code breaks if `FOLDS_AMOUNT` changes as generator is unpacked using 5 hardcoded values (temporary solution)
FOLDS_AMOUNT = 3
INPUT_LOC = "./data/combo.json"
OUTPUT_LOC = "scratch_metrics/combo_model"
MODEL_DIR = INPUT_LOC.split('/')[-1].split('.')[0]
MODEL_NAME = MODEL_DIR.split('_')[0]
BASE_DATA_LOC = "./data/baseline_model/stopwords_nltk_func_fysio.json"
COMPARE_WITH_BASE = False

#Variables
total_training_results = []
total_dev_results = []

if __name__ == "__main__":
    data = import_data(INPUT_LOC)
    baseline_streaks = None
    if COMPARE_WITH_BASE:
        baseline_streaks = import_data_csv_to_streak("./data/scratch_metrics/baseline_model/res_fold_0_base_func_fysio_dev.csv")
    
    #TODO: temporary solution, unpacking with 3 variables 
    first_fold, second_fold, third_fold = generate_training_test_folds(FOLDS_AMOUNT, data)#, fourth_fold, fifth_fold  = 
    fold_list = []
    fold_list.append(first_fold)
    fold_list.append(second_fold)
    fold_list.append(third_fold)

    for fold_idx in range(FOLDS_AMOUNT):
        print(f"FOLD {fold_idx}")
        train_ds, val_ds = retrieve_training_test_data(fold_list[fold_idx], data)
        transformed_train_ds = transform_dataset(train_ds[0], train_ds[1])
        transformed_val_ds = transform_dataset(val_ds[0], val_ds[1])
 
        model = tf.keras.models.Sequential([
            tf.keras.layers.Embedding(50, 8, input_length=40),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(3, activation='softmax')
        ])
        model.compile(optimizer='adam', 
                      loss="categorical_crossentropy", 
                      metrics=[keras.metrics.Precision(), keras.metrics.Recall(), f1_metric]
                      )
        history = model.fit(
            transformed_train_ds[0], 
            transformed_train_ds[1], 
            validation_data=transformed_val_ds, 
            epochs=6, 
            batch_size=2, 
            verbose=0
            )
        if fold_idx == 0:
            results_per_epoch_train = transform_tf_history_data(history.history["f1_metric"], history.history["precision"], history.history["recall"], history.history["loss"])
            results_per_epoch_dev = transform_tf_history_data(history.history["val_f1_metric"], history.history["val_precision"], history.history["val_recall"], history.history["val_loss"])
        else:
            results_per_epoch_train = transform_tf_history_data(history.history["f1_metric"], history.history[f"precision_{fold_idx}"], history.history[f"recall_{fold_idx}"], history.history[f"loss"])
            results_per_epoch_dev = transform_tf_history_data(history.history["val_f1_metric"], history.history[f"val_precision_{fold_idx}"], history.history[f"val_recall_{fold_idx}"], history.history[f"val_loss"])
        total_training_results.append(results_per_epoch_train)
        total_dev_results.append(results_per_epoch_dev)
        export_data(f"./data/{OUTPUT_LOC}/res_fold_{fold_idx +1}_{MODEL_DIR}_train.csv", results_per_epoch_train, fold_idx)
        export_data(f"./data/{OUTPUT_LOC}/res_fold_{fold_idx +1}_{MODEL_DIR}_dev.csv", results_per_epoch_dev, fold_idx)
    data_avg_total_train = compute_avg_training_epochs(total_training_results)
    data_avg_total_dev = compute_avg_training_epochs(total_dev_results)
    data_avg_streaks_train = transform_training_epoch_list_to_streak(data_avg_total_train)
    data_avg_streaks_dev = transform_training_epoch_list_to_streak(data_avg_total_dev)
    #plot_results(f"{MODEL_NAME} Model statistics", data_avg_streaks_train, baseline_streaks)
    #plot_results(f"{MODEL_NAME} Model statistics", data_avg_streaks_dev, baseline_streaks)
    export_data(f"./data/{OUTPUT_LOC}/res_AVG_{MODEL_DIR}_train.csv", data_avg_total_train)
    export_data(f"./data/{OUTPUT_LOC}/res_AVG_{MODEL_DIR}_dev.csv", data_avg_total_dev)