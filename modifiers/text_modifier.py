import spacy
import nltk
from nltk.stem.snowball import SnowballStemmer
from spacy.lang.nl.examples import sentences
from string import punctuation

nlp = spacy.load("nl_core_news_sm")

class TextModifier():
    @staticmethod
    def apply_lemmatization(paragraph_text: str) -> str:
        #these puncts should be attached to preceding word
        punct_list = ".!,;:]}\\/)?"
        doc = nlp(paragraph_text)
        modified_paragraph = ""
        for word in doc:
            #if word is punctuation, remove trailing whitespace if applicaple
            if word.lemma_ in punct_list:
                modified_paragraph = modified_paragraph.rstrip()
            modified_paragraph = modified_paragraph + word.lemma_ + " "
        modified_paragraph = modified_paragraph.rstrip()
        return modified_paragraph

    @staticmethod
    def apply_stemming(paragraph_text: str) -> str:
        stemmer = SnowballStemmer("dutch")
        modified_paragraph = ""
        for word in paragraph_text.split():
            modified_paragraph += stemmer.stem(word) + " "
        modified_paragraph.rstrip()
        return modified_paragraph

    @staticmethod
    def remove_stop_words(paragraph_text: str, stopwords) -> str:
        # functions used to normalize words
        def remove_punctuation(chars):
            return chars.translate(str.maketrans('', '', punctuation))

        def to_lower(word):
            return str.lower(word)

        # read all words as a list, this list will be modified along the loop
        text = paragraph_text.split(' ')
        return_list = []
        # the following loop directly removes a word from `text` if the word is found in the `stopwords` list
        for index, word in enumerate(text):
            # words must be normalized so that it can be matched with the stopwords list
            normalized_word = to_lower(remove_punctuation(word))

            if normalized_word not in stopwords:
                return_list.append(text[index])  # delete entry from `text` by index

        return ' '.join(return_list)
