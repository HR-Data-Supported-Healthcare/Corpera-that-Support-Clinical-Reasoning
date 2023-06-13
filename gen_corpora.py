"""
Basic ETL proces to create a corpora ready for annotation (NER) step.
Unoptimized.
docx data should be stored in `DATA_DIR` destination for file to work
output directory should be stored in constant `OUTPUT_DIR`
"""

from datetime import datetime
from pipeline_config_system import PipelineConfigSystem
from etl_classes.demo_etl import DemoETL
from etl_classes.aggregate_etl import AggregateETL
from etl_classes.dynamic_etl import DynamicETL
from init_source_dest_dir import init_source_dest_dirs
from data_classes.flag import ParagraphFlags, TextFlags, FlagContainer
from data_classes.etl_pipelines import PipelineType

#CONSTANTS
USE_PIPELINE_CONFIG_SYSTEM = True
DATA_DIR =  "./data"
OUTPUT_DIR = "./output"

#FUNCTIONS
def use_demo_etl():
    DemoETL(DATA_DIR, f"{OUTPUT_DIR}/Demo {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json")

def use_dynamic_etl(config: FlagContainer):
    DynamicETL(DATA_DIR, f"{OUTPUT_DIR}/Dyna {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json", config)

def use_aggregate_etl():
    AggregateETL(DATA_DIR, f"{OUTPUT_DIR}/Aggre {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.docx")

def execute_pipelines():
    default_paragraph_flags = ParagraphFlags()
    default_text_flags = TextFlags()
    default_flags = FlagContainer(default_paragraph_flags, default_text_flags)
    pipeline, flags = PipelineConfigSystem.configure_pipeline_and_flags(default_flags, USE_PIPELINE_CONFIG_SYSTEM)
    if pipeline == PipelineType.DEFAULT_DYNAMIC or PipelineType.CUSTOM_DYNAMIC:
        use_dynamic_etl(flags)
    elif pipeline == PipelineType.DEMO:
        use_demo_etl()

if __name__ == "__main__":
    init_source_dest_dirs(DATA_DIR, OUTPUT_DIR) # checks whether the source and destination files exist
    execute_pipelines()
