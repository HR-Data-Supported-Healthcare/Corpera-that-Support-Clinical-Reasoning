import spacy;
from spacy.lang.nl.examples import sentences;

class ParagraphModifier():
    @staticmethod
    def lemmatisation(paragraph_text: str) -> str:
        nlp = spacy.load("nl_core_news_sm")
        doc = nlp(paragraph_text)
        modified_paragraph = paragraph_text
        for word in doc:
            if word.pos_ == "VERB":
                print(word, word.lemma_)
                modified_paragraph = modified_paragraph.replace(f"{word}", f"{word.lemma_}")
        return modified_paragraph

    @staticmethod
    def stemming(paragraph_text: str) -> str:
        pass

    @staticmethod
    def remove_heading(paragraph_text: dict) -> dict:
        pass

    @staticmethod
    def remove_stop_words(stop_words: list[str], paragraph_text: str) -> str:
        #loop through text, remove words from text that are in stop_words list 
        #return text
        pass

    text = "Het schrijven van dit zorgverslag zorgde voor een verdere ontwikkeling van diverse competenties en daarbij leerde ik kijken naar de zorg met een kritische blik. Ik vond het interessant om vanaf de opname te zien hoe belangrijk het is om dan al goed te starten met het verzamelen van gegevens voor de vervolgstappen. Ook vond ik het interessant om mee te denken in het stellen van de diagnoses en doelen en de manier waarop deze behaald gaan worden. Het maken van dit zorgverslag benadrukte voor mij, dat ik de juiste keuze heb gemaakt om mezelf te gaan ontwikkelen tot een verpleegkundige op HBO niveau. De casus waaruit ik dit zorgverslag gemaakt heb, is een casus die genomen is aan het begin van mijn ervaring in het ziekenhuis. Toch kwam ik, tijdens het evalueren van de zorg, erachter dat ik veel heb kunnen betekenen in de uitvoering van zorg tijdens deze opname. "
    lemmatisation(text)
