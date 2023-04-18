"""
Basic ETL proces to create a corpora ready for annotation (NER) step.
Unoptimized.
docx data should be stored in `DATA_DIR` destination for file to work
output directory should be stored in constant `OUTPUT_DIR`
"""

from datetime import datetime
from etl_classes import DemoETL, AggregateETL, DynamicETL

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
    DemoETL(DATA_DIR, f"{OUTPUT_DIR}/Demo {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json")

def use_dynamic_etl():
    DynamicETL(DATA_DIR, f"{OUTPUT_DIR}/Dynamic {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.docx")

def use_aggregate_etl():
    AggregateETL(DATA_DIR, f"{OUTPUT_DIR}/Aggre {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.docx")

if __name__ == "__main__":
    ###Select which pipeline to use (uncomment)
    #use_demo_etl()
    use_aggregate_etl()