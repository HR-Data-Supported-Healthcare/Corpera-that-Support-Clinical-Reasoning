"""
Basic ETL proces to create a corpora ready for annotation (NER) step.
Unoptimized.
docx data should be stored in `DATA_DIR` destination for file to work
output directory should be stored in constant `OUTPUT_DIR`
"""

from datetime import datetime
from etl_classes import DemoETL, AggregateETL

#TODO: "Implement flags
#TODO: Comments/docstrings

#CONSTANTS
LEMMATIZATION_FLAG = False
STEMMING_FLAG = False
STOP_WORDS_FLAG = False

DATA_DIR =  "./data"
OUTPUT_DIR = "./output"

#FUNCTIONS
def use_demo_etl():
    extracted_data = DemoETL.extract(DATA_DIR)
    transformed_data = DemoETL.transform(extracted_data)
    DemoETL.load(f"{OUTPUT_DIR}/Demo {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json", transformed_data)

def use_dynamic_etl():
    pass

def use_aggregate_etl():
    extracted_data = AggregateETL.extract(DATA_DIR)
    print(extracted_data)
    transformed_data = AggregateETL.transform(extracted_data)
    AggregateETL.load(f"{OUTPUT_DIR}/Aggre {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.docx", transformed_data)

if __name__ == "__main__":
    #Select which pipeline to use (uncomment)
    use_demo_etl()
    #use_aggregate_etl()