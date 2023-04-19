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
