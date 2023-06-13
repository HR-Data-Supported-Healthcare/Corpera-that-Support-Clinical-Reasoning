"""TODO: Docstring"""
from data_classes.flag import FlagContainer, TextFlags, ParagraphFlags
from data_classes.etl_pipelines import PipelineType
import json

class PipelineConfigSystem:
    @staticmethod
    def ask_for_pipeline() -> PipelineType:
        while True:
            print('\n'*100)
            print("--- Which ETL pipeline would you like to use? (1/2/3) ---")
            print("1.\t Dynamic ETL with default settings\n2.\t Dynamic ETL with custom settings\n3.\t Demo ETL")
            match input("Pipeline: "):
                case "1":
                    print("Using default parameters for ETL...")
                    return PipelineType.DEFAULT_DYNAMIC
                case "2":
                    return PipelineType.CUSTOM_DYNAMIC
                case "3":
                    return PipelineType.DEMO
                case _:
                    print("Invalid answer.")

    def configure_flag(question: str) -> bool:
        while True:
            user_answer = input(question + " (y/n) ")
            match user_answer.lower():
                case "y": return True
                case "n": return False
                case _: print("Invalid answer. Please answer with 'y' or 'n'.")

    def configure_from_flags(flag_dict: dict) -> dict:
        default_question = "Do you want to "
        for key in flag_dict:
            if key == "apply_lemmatization" and flag_dict["apply_stemming"]:
                flag_dict[key] = False
                continue
            split_key = key.split("_")
            cleaned_key = " ".join(split_key).rstrip()
            specific_question = default_question + cleaned_key + "?"
            flag_dict[key] = PipelineConfigSystem.configure_flag(specific_question)
        return flag_dict

    @staticmethod
    def configure_dynamic_etl(flags: FlagContainer):
        print('\n'*100)
        print('--- Define the parameters ---')
        #create dictionary output so that we can access the keys (used for generating questions)
        text_flags_json_str =  json.dumps(flags.text_flags.__dict__)
        text_flags_json_object = json.loads(text_flags_json_str)
        text_flags_json_object = PipelineConfigSystem.configure_from_flags(text_flags_json_object)
        para_flags_json_str = json.dumps(flags.paragraph_flags.__dict__)
        para_flags_json_object = json.loads(para_flags_json_str)
        para_flags_json_object = PipelineConfigSystem.configure_from_flags(para_flags_json_object)

        #transform dicts back to respective classes
        updated_text_flags = TextFlags(**text_flags_json_object)
        updated_para_flags = ParagraphFlags(**para_flags_json_object)
        return FlagContainer(updated_para_flags, updated_text_flags)

    @staticmethod
    def configure_pipeline_and_flags(default_flags: FlagContainer, use_system: bool) -> tuple[PipelineType, FlagContainer]:
        if not use_system:
            return PipelineType.DEFAULT_DYNAMIC, default_flags
        chosen_pipeline = PipelineConfigSystem.ask_for_pipeline()
        #No need for further configuration with these outputs
        if chosen_pipeline == PipelineType.DEFAULT_DYNAMIC or chosen_pipeline == PipelineType.DEMO:
            return chosen_pipeline, default_flags
        custom_flags = PipelineConfigSystem.configure_dynamic_etl(default_flags)
        return chosen_pipeline, custom_flags