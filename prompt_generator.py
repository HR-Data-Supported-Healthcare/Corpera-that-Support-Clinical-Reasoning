class PromptSystem:
    def __init__(self):
        self.user_answers = {"LEMMATIZATION_FLAG": False, "STEMMING_FLAG": False, "STOP_WORDS_FLAG": False, "REMOVE_HEADINGS_FLAG": False}
        self.prompts = [
            {"text": "Do you want to use lemmatization?", "key": "LEMMATIZATION_FLAG"},
            {"text": "Do you you want to use stemming", "key": "STEMMING_FLAG"},
            {"text": "Do you want to remove stop words?", "key": "STOP_WORDS_FLAG"},
            {"text": "Do you want to remove headings?", "key": "REMOVE_HEADINGS_FLAG"}
        ]

    def ask_question(self, prompt):
        skip_stemming = False
        while True:
            print('\n'*100)

            if prompt["key"] == "STEMMING_FLAG" and skip_stemming:
                continue
            
            answer = input(prompt["text"] + " (y/n) ")

            if answer.lower() == "y":
                self.user_answers[prompt["key"]] = True
                if prompt["key"] == "LEMMATIZATION_FLAG":
                    skip_stemming = True
                break
            
            elif answer.lower() == "n":
                self.user_answers[prompt["key"]] = False
                break
            
            else:
                print("Invalid answer. Please answer with 'y' or 'n'.")
        
        print("User answers:", self.user_answers)
    
    def run(self):
        for prompt in self.prompts:
            self.ask_question(prompt)