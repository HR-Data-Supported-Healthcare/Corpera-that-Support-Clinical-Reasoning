from datetime import datetime
from pipeline_config_system import PipelineConfigSystem
from etl_classes.demo_etl import DemoETL
from etl_classes.aggregate_etl import AggregateETL
from etl_classes.dynamic_etl import DynamicETL
from init_source_dest_dir import init_source_dest_dirs
from data_classes.flag import ParagraphFlags, TextFlags, FlagContainer
from data_classes.etl_pipelines import PipelineType

# CONSTANTS
USE_PIPELINE_CONFIG_SYSTEM = True
DATA_DIR =  "./data"
OUTPUT_DIR = "./output"

def use_demo_etl() -> None:
    """Executes the DemoETL process to transform data and save the output in JSON format."""
    DemoETL(DATA_DIR, f"{OUTPUT_DIR}/Demo {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json")

def use_dynamic_etl(config: FlagContainer) -> None:
    """
    Executes the DynamicETL process to dynamically transform data based on the provided configuration
    and save the output in JSON format.

    Args:
        config (FlagContainer): Configuration flags for paragraph and text processing.
    """
    DynamicETL(DATA_DIR, f"{OUTPUT_DIR}/Dyna {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.json", config)

def use_aggregate_etl() -> None:
    """Executes the AggregateETL process to aggregate data and save the output in DOCX format."""
    AggregateETL(DATA_DIR, f"{OUTPUT_DIR}/Aggre {datetime.now().strftime('%m-%d-%Y,%H-%M-%S')}.docx")

def execute_pipelines() -> None:
    """
    Determines and executes the appropriate ETL pipeline based on the configuration.

    The pipeline type is configured using the PipelineConfigSystem. If the pipeline is a default or
    custom dynamic pipeline, the use_dynamic_etl() function is called with the corresponding flags.
    If the pipeline is a demo pipeline, the use_demo_etl() function is called.
    """
    default_paragraph_flags = ParagraphFlags()
    default_text_flags = TextFlags()
    default_flags = FlagContainer(default_paragraph_flags, default_text_flags)
    pipeline, flags = PipelineConfigSystem.configure_pipeline_and_flags(default_flags, USE_PIPELINE_CONFIG_SYSTEM)
    if pipeline == PipelineType.DEFAULT_DYNAMIC or pipeline == PipelineType.CUSTOM_DYNAMIC:
        use_dynamic_etl(flags)
    elif pipeline == PipelineType.DEMO:
        use_demo_etl()

if __name__ == "__main__":
    init_source_dest_dirs(DATA_DIR, OUTPUT_DIR) # checks whether the source and destination files exist
    execute_pipelines()
