from modifiers.text_modifier import TextModifier
import unittest

# hardcoded list of stopwords
stopwords_list = [
    "de",
    "het",
    "een",
    "bij",
    "deze",
    "te",
    "was",
    "dit",
    "voor",
    "ook",
    "om",
    "dat",
    "maar"
]

remove_stopwords = lambda string : TextModifier.remove_stop_words(string, stopwords_list)

class TestRemoveStopWords(unittest.TestCase):
    def test_remove_stopwords(self):
        # ARRANGE
        source_string = "Doordat deze ziekte lastig was vast te stellen zorgde dit voor veel \
            vragen en spanningen bij de patiënt en het zorgpersoneel en ook bij mij. \
            Ik vond het lastig om te zien dat iemand achteruit blijft gaan, maar dat het zoeken is naar de oorzaak."

        # ACT
        string_with_no_stopwords = remove_stopwords(source_string)
        
        # ASSERT
        expected_output = "Doordat ziekte lastig vast stellen zorgde veel \
            vragen en spanningen patiënt en zorgpersoneel en mij. \
            Ik vond lastig zien iemand achteruit blijft gaan, zoeken is naar oorzaak."
        
        assert string_with_no_stopwords == expected_output

    def test_remove_empty_string(self):
        # ARRANGE
        source_string = ""

        # ACT
        result = remove_stopwords(source_string)

        # ASSERT
        assert result == ""
