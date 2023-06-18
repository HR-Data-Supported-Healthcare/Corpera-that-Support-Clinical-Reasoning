import spacy
import nltk
from nltk.stem.snowball import SnowballStemmer
from spacy.lang.nl.examples import sentences
from string import punctuation

nlp = spacy.load("nl_core_news_lg")

class TextModifier():
    @staticmethod
    def apply_lemmatization(paragraph_text: str) -> str:
        """
        Apply lemmatization to the given paragraph text.

        Args:
            paragraph_text (str): The paragraph text.

        Returns:
            str: The modified paragraph text after lemmatization.
        """
        # These puncts should be attached to the preceding word
        punct_list = ".!,;:]}\\/)?"
        doc = nlp(paragraph_text)
        modified_paragraph = ""
        for word in doc:
            # If word is punctuation, remove trailing whitespace if applicable
            if word.lemma_ in punct_list:
                modified_paragraph = modified_paragraph.rstrip()
            modified_paragraph = modified_paragraph + word.lemma_ + " "
        modified_paragraph = modified_paragraph.rstrip()
        return modified_paragraph

    @staticmethod
    def apply_stemming(paragraph_text: str) -> str:
        """
        Apply stemming to the given paragraph text.

        Args:
            paragraph_text (str): The paragraph text.

        Returns:
            str: The modified paragraph text after stemming.
        """
        stemmer = SnowballStemmer("dutch")
        modified_paragraph = ""
        for word in paragraph_text.split():
            modified_paragraph += stemmer.stem(word) + " "
        modified_paragraph.rstrip()
        return modified_paragraph

    @staticmethod
    def remove_stop_words(paragraph_text: str, stopwords) -> str:
        """
        Remove stop words from the given paragraph text.

        Args:
            paragraph_text (str): The paragraph text.
            stopwords: The list of stop words to be removed.

        Returns:
            str: The modified paragraph text after stop word removal.
        """
        # Read all words as a list, this list will be modified along the loop
        text = paragraph_text.split(' ')
        return_list = []
        # The following loop directly removes a word from `text` if the word is found in the `stopwords` list
        for index, word in enumerate(text):
            # Words must be normalized so that they can be matched with the stop words list
            normalized_word = TextModifier.remove_punctuation(word).lower()

            if normalized_word not in stopwords:
                return_list.append(text[index])  # Delete entry from `text` by index

        return ' '.join(return_list)

    @staticmethod
    def remove_punctuation(paragraph_text: str, punctuation_list: list[str]=punctuation) -> str:
        """
        Remove punctuation from the given paragraph text.

        Args:
            paragraph_text (str): The paragraph text.
            punctuation_list (list[str], optional): List of punctuation characters to be removed. Defaults to string.punctuation.

        Returns:
            str: The modified paragraph text after punctuation removal.
        """
        return paragraph_text.translate(str.maketrans('', '', punctuation))
