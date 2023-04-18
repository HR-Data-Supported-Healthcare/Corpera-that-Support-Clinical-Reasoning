"""
Basic ETL proces to create a corpora ready for annotation (NER) step.
Unoptimized.
docx data should be stored in `DATA_DIR` destination for file to work
output directory should be stored in constant `OUTPUT_DIR`
"""

from datetime import datetime
from prompt_generator import PromptSystem
from etl_classes import DemoETL, AggregateETL

#TODO: "Implement flags
#TODO: Comments/docstrings

#CONSTANTS
flag_dict = {
"stop_words": False,
"lemmatisation": False,
"stemming": False,
"heading": False
}

DATA_DIR =  "./data"
OUTPUT_DIR = "./output"

#FUNCTIONS
def use_demo_etl():
    DemoETL(DATA_DIR, f"{OUTPUT_DIR}/Demo {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json")

def use_dynamic_etl():
    pass

def use_aggregate_etl():
    AggregateETL(DATA_DIR, f"{OUTPUT_DIR}/Aggre {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.docx")

def set_flags(user_answers):
    global flag_dict

    flag_dict["lemmatisation"] = user_answers["LEMMATIZATION_FLAG"]
    flag_dict["stemming"] = user_answers["STEMMING_FLAG"]
    flag_dict["stop_words"] = user_answers["STOP_WORDS_FLAG"]
    flag_dict["heading"] = user_answers["HEADINGS_FLAG"]

if __name__ == "__main__":
    prompt_system = PromptSystem()
    prompt_system.run()
    set_flags(prompt_system.user_answers)
    
    ###Select which pipeline to use (uncomment)
    #use_demo_etl()
    use_aggregate_etl()