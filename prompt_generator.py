class PromptSystem:

    def __init__(self):
        self.user_answers = {"LEMMATIZATION_FLAG": False, "STEMMING_FLAG": False,
                             "STOP_WORDS_FLAG": False, "HEADINGS_FLAG": False, "BIBLIOGRAPFY_FLAG": False}
        self.prompts = [
            {"text": "Do you want to use lemmatization?",
                "key": "LEMMATIZATION_FLAG"},
            {"text": "Do you you want to use stemming", "key": "STEMMING_FLAG"},
            {"text": "Do you want to remove stop words?", "key": "STOP_WORDS_FLAG"},
            {"text": "Do you want to remove headings?", "key": "HEADINGS_FLAG"},
            {"text": "Do you want to remove the bibliography?",
                "key": "BIBLIOGRAPFY_FLAG"}
        ]
        self.skip_stemming = False

    def ask_question(self, prompt):
        while True:

            if prompt["key"] == "STEMMING_FLAG" and self.skip_stemming:
                break

            answer = input(prompt["text"] + " (y/n) ")

            if answer.lower() == "y":
                self.user_answers[prompt["key"]] = True
                if prompt["key"] == "LEMMATIZATION_FLAG":
                    self.skip_stemming = True
                break

            elif answer.lower() == "n":
                self.user_answers[prompt["key"]] = False
                break

            else:
                print("Invalid answer. Please answer with 'y' or 'n'.")

    def run(self):
        chosen_pipeline = self.ask_for_pipeline()

        if chosen_pipeline == "DYNAMIC_ETL":
            self.set_default_settings()
            return 'DYNAMIC_ETL'

        if chosen_pipeline == "DEMO_ETL":
            return 'DEMO_ETL'

        if chosen_pipeline == "CUSTOM_DYNAMIC_ETL":
            print('\n'*100)
            print('--- Define the parameters ---')
            for prompt in self.prompts:
                self.ask_question(prompt)
            return 'DYNAMIC_ETL'

    def ask_for_pipeline(self):
        while True:
            print('\n'*100)
            print("--- Which ETL pipeline would you like to use? (1/2/3) ---")
            print(
                "1.\t Dynamic ETL with default settings\n2.\t Dynamic ETL with custom settings\n3.\t Demo ETL")
            pipeline = input("Pipeline: ")

            if pipeline.lower() == "1":
                print("Using default parameters for ETL...")
                return "DYNAMIC_ETL"

            if pipeline.lower() == "2":
                return "CUSTOM_DYNAMIC_ETL"

            if pipeline.lower() == "3":
                return "DEMO_ETL"

            else:
                print("Invalid answer.")

    def set_default_settings(self):
        self.user_answers["LEMMATIZATION_FLAG"] = True
        self.user_answers["STOP_WORDS_FLAG"] = True
        self.user_answers["HEADINGS_FLAG"] = True
        self.user_answers["BIBLIOGRAPFY_FLAG"] = True
