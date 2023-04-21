"""
Basic ETL proces to create a corpora ready for annotation (NER) step.
Unoptimized.
docx data should be stored in `DATA_DIR` destination for file to work
output directory should be stored in constant `OUTPUT_DIR`
"""

from datetime import datetime
from prompt_generator import PromptSystem
from etl_classes.demo_etl import DemoETL
from etl_classes.aggregate_etl import AggregateETL
from etl_classes.dynamic_etl import DynamicETL
from init import init

#TODO: "Implement flags
#TODO: Comments/docstrings

#CONSTANTS
LEMMATIZATION_FLAG = False
STEMMING_FLAG = False
STOP_WORDS_FLAG = False
HEADINGS_FLAG = True
BIBLIOGRAPFY_FLAG = False

#CONFIG = {"stop_words" : STOP_WORDS_FLAG, "stemming" : STEMMING_FLAG, "lemmatization": LEMMATIZATION_FLAG,}
CONFIG = {"paragraph_filters" : { "headings": HEADINGS_FLAG, "bibliography" : BIBLIOGRAPFY_FLAG},
        "text_transformations" : 
          {"stop_words" : STOP_WORDS_FLAG, "stemming" : STEMMING_FLAG, "lemmatization": LEMMATIZATION_FLAG}
          }

DATA_DIR =  "./data"
OUTPUT_DIR = "./output"

#FUNCTIONS
def use_demo_etl():
    DemoETL(DATA_DIR, f"{OUTPUT_DIR}/Demo {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json")

def use_dynamic_etl():
    DynamicETL(DATA_DIR, f"{OUTPUT_DIR}/Dyna {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json", CONFIG)

def use_aggregate_etl():
    AggregateETL(DATA_DIR, f"{OUTPUT_DIR}/Aggre {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.docx")

def set_flags(user_answers):
    global CONFIG

    CONFIG["text_transformations"]["lemmatization"] = user_answers["LEMMATIZATION_FLAG"]
    CONFIG["text_transformations"]["stop_words"] = user_answers["STOP_WORDS_FLAG"]
    CONFIG["paragraph_filters"]["headings"] = user_answers["HEADINGS_FLAG"]
    CONFIG["paragraph_filters"]["bibliography"] = user_answers["BIBLIOGRAPFY_FLAG"]
    CONFIG["text_transformations"]["stemming"] = user_answers["STEMMING_FLAG"]

def choose_pipeline():
    prompt_system = PromptSystem()
    pipeline = prompt_system.run()
    set_flags(prompt_system.user_answers)

    if pipeline == 'DYNAMIC_ETL':
        use_dynamic_etl()
        
    if pipeline == 'DEMO_ETL':
        use_demo_etl()


if __name__ == "__main__":
    init(DATA_DIR, OUTPUT_DIR) # checks whether the source and destination files exist

    #Comment this function, if you do not want to use the prompt system
    choose_pipeline()

    # ###Manually select which pipeline to use (uncomment)
    # use_demo_etl()
    # use_aggregate_etl()
    # use_dynamic_etl()