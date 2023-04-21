class PromptSystem:
    def __init__(self):
        self.user_answers = {"LEMMATIZATION_FLAG": False, "STEMMING_FLAG": False, "STOP_WORDS_FLAG": False, "HEADINGS_FLAG": False, "BIBLIOGRAPFY_FLAG": False}
        self.prompts = [
            {"text": "Do you want to use lemmatization?", "key": "LEMMATIZATION_FLAG"},
            {"text": "Do you you want to use stemming", "key": "STEMMING_FLAG"},
            {"text": "Do you want to remove stop words?", "key": "STOP_WORDS_FLAG"},
            {"text": "Do you want to remove headings?", "key": "HEADINGS_FLAG"},
            {"text": "Do you want to remove the bibliography?", "key": "BIBLIOGRAPFY_FLAG"}
        ]
        self.skip_stemming = False

    def ask_question(self, prompt):
        while True:
            print('\n'*100)

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
        
        print("User answers:", self.user_answers)
    
    def run(self):
        use_default_settings = self.ask_for_default_settings()

        if(use_default_settings):
            self.set_default_settings()
            return 'AGGREGATE_ETL'
        
        use_demo_etl = self.ask_for_demo_etl()
            
        if(use_demo_etl):
            return 'DEMO_ETL'

        for prompt in self.prompts:
            self.ask_question(prompt)
            return 'AGGREGATE_ETL'


    def ask_for_default_settings(self):
        demo_etl = input("Do you want to use the default ETL-settings? (y/n)")
        while True:
            if demo_etl.lower() == "y":
                print("Using default parameters for ETL...")
                return True
            if demo_etl.lower() == "n":
                return False
            
    def ask_for_demo_etl(self):
        demo_etl = input("Do you want to use the Demo ETL? (y/n)")
        while True:
            if demo_etl.lower() == "y":
                print("Using Demo ETL...")
                return True
            if demo_etl.lower() == "n":
                return False
            
    def set_default_settings(self):
        self.user_answers["LEMMATIZATION_FLAG"] = True
        self.user_answers["STOP_WORDS_FLAG"] = True
        self.user_answers["HEADINGS_FLAG"] = True
        self.user_answers["BIBLIOGRAPFY_FLAG"] = True
        




        
        