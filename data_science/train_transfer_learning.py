from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
import torch
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from .utils import generate_training_test_folds, import_data, retrieve_training_test_data
import csv

#Classes
class FunctionerenDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)
    
#Functions
def compute_metrics(pred):
    global ita_training_results
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='weighted')
    acc = accuracy_score(labels, preds)
    training_res = {'accuracy': acc, 'f1': f1, 'precision': precision, 'recall': recall }
    ita_training_results.append(training_res)
    return training_res

def compute_avg(folds_training_results: list[list[dict]])-> dict:
    print("[computing avg]")
    epoch_amt = len(folds_training_results[0])
    fold_amt = len(folds_training_results)
    acc_sum = [0 for _ in range(len(folds_training_results[0]))]
    f1_sum = [0 for _ in range(len(folds_training_results[0]))]
    p_sum = [0 for _ in range(len(folds_training_results[0]))]
    r_sum = [0 for _ in range(len(folds_training_results[0]))]
    for res in folds_training_results:
        for epoch_indx in range(epoch_amt):
            acc_sum[epoch_indx] += res[epoch_indx]["accuracy"]
            f1_sum[epoch_indx] += res[epoch_indx]["f1"]
            p_sum[epoch_indx] += res[epoch_indx]["precision"]
            r_sum[epoch_indx] += res[epoch_indx]["recall"]
    acc_avg = [acc_s / fold_amt for acc_s in acc_sum]
    f1_avg = [f1_s / fold_amt for f1_s in f1_sum]
    p_avg = [p_s / fold_amt for p_s in p_sum]
    r_avg = [r_s / fold_amt for r_s in r_sum]
    return_list = []
    for i in range(epoch_amt):
        return_list.append({'accuracy': acc_avg[i], 'f1': f1_avg[i] , 'precision': p_avg[i] , 'recall': r_avg[i]})
    return return_list

def export_data(data_dir: str, data: dict, fold: int = -1) -> None:
    print("[exporting dataset]")
    with open(data_dir, 'w', newline='') as f:
        fieldnames = ['fold', 'epoch', 'accuracy', 'f1', 'precision', 'recall']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i, d in enumerate(data):
            d["epoch"] = i +1
            d["fold"] = fold +1
            writer.writerow(d)

#Constants
TRAINING_ARGS = TrainingArguments(
    output_dir='./results',
    num_train_epochs=5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=16,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy="epoch"
)
#Code breaks if `FOLDS_AMOUNT` changes as generator is unpacked using 5 hardcoded values (temporary solution)
FOLDS_AMOUNT = 5
INPUT_LOC = "../data/combo.json"

#Variables
ita_training_results = []
total_training_results = []

def transform_dataset_to_functioneren(tokenizer, X_features: list[str], y_labels: list[int]):
    tokenized_features = tokenizer(X_features, truncation=True, padding=True)
    return FunctionerenDataset(tokenized_features, y_labels.tolist())

if __name__ == "__main__":
    tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robbert-v2-dutch-base")
    data = import_data(INPUT_LOC)
    #TODO: temporary solution, unpacking with 5 variables 
    first_fold, second_fold, third_fold, fourth_fold, fifth_fold  = generate_training_test_folds(FOLDS_AMOUNT, data) #
    fold_list = []
    fold_list.append(first_fold)
    fold_list.append(second_fold)
    fold_list.append(third_fold)
    fold_list.append(fourth_fold)
    fold_list.append(fifth_fold)

    for fold_idx in range(FOLDS_AMOUNT):
        print(f"FOLD {fold_idx}")
        train_ds, val_ds = retrieve_training_test_data(fold_list[fold_idx], data)
        train_dataset = transform_dataset_to_functioneren(tokenizer, train_ds[0], train_ds[1])
        val_dataset = transform_dataset_to_functioneren(tokenizer, val_ds[0], val_ds[1])
        model = RobertaForSequenceClassification.from_pretrained("pdelobelle/robbert-v2-dutch-base", num_labels=3)
        trainer = Trainer(
            model=model,
            args=TRAINING_ARGS,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            compute_metrics=compute_metrics,
        )
        trainer.train()
        total_training_results.append(ita_training_results)
        ita_training_results = []
    for i_fold, res in enumerate(total_training_results):
        export_data(f"../data/res_fold_{i_fold}_{INPUT_LOC.split('/')[-1].split('.')[0]}.csv", res, i_fold)
    data_avg = compute_avg(total_training_results)
    export_data(f"../data/transfer_learning_metrics/res_AVG_{INPUT_LOC.split('/')[-1].split('.')[0]}.csv", data_avg)
    #trainer.save_model("./model_02_shuffle_no_warmup")