import json
import os
import sys

INPUT_DIR = "./to_transform"
OUTPUT_DIR = "./transformed/corpus2.json"

def calculate_total_paragraphs(contents):
    total = 0
    for p in contents["documents"]:
        for _ in p["corpora"]:
            total += 1
    print("Total paragraphs " + str(total))

def generate_doccano_format_per_file(contents):
    for p in contents["documents"]:
        total_file = []
        for c in p["corpora"]:
            total_file.append({"text" : c["text"], "label" : []})
        with open(f"./to_annotate/{p['filename']}.json", "w") as f:
            f.write(json.dumps(total_file))

def generate_total_format(contents):
    total = []
    for p in contents["documents"]:
        for c in p["corpora"]:
            total.append({"text" : c["text"], "label" : []})
    
    with open("./preprocessed_data.json", "w") as f:
        f.write(json.dumps(total))

def transform_doccano_to_filter(data):
    filtered_data = []
    for d in data:
        filtered_data.append({"text": d["text"], "label": d["label"]})
    return filtered_data

def transform_annots_to_numeric(data):
    for d in data:
        if d["label"][0] == "patient_functioneren": d["label"] = 0
        elif d["label"][0] == "patient_overig":     d["label"] = 1
        elif d["label"][0] == "overig":             d["label"] = 2
    return data

def transform_all_documents(data_dir):
    total_data = []
    for filename in os.listdir(data_dir):
        with open(f"{data_dir}/{filename}", "r", 
                  encoding="utf-8") as f:
            data = json.load(f)
        data = transform_annots_to_numeric(data)    
        data = transform_doccano_to_filter(data)
        total_data.extend(data)
    return total_data

def save_json(data, file_dest_name) -> None:
    with open(file_dest_name, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        INPUT_DIR = sys.argv[0]
        OUTPUT_DIR = sys.argv[1]
    elif len(sys.argv) != 0:
        #TODO: throw error 
        exit()
    data = transform_all_documents(INPUT_DIR)
    save_json(data, OUTPUT_DIR)