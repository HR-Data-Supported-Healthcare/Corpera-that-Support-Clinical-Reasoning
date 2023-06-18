import unittest
from modifiers.text_modifier import TextModifier


class TestStemming(unittest.TestCase):
    def test_stemming(self):
        # ARRANGE
        source_string = "Vanochtend ben ik vroeg opgestaan en heb ik een lekkere kop koffie gezet. Vervolgens heb ik mijn tanden gepoetst en ben ik naar buiten gegaan om een stuk te gaan hardlopen. Na het rennen heb ik gedoucht en me aangekleed."

        # ACT
        stemmed_text = TextModifier.apply_stemming(source_string)

        # ASSERT
        expected_output = "vanocht ben ik vroeg opgestan en heb ik een lekker kop koffie gezet. vervolgen heb ik mijn tand gepoetst en ben ik nar buit gegan om een stuk te gan hardlopen. na het renn heb ik gedoucht en me aangekleed."

        assert stemmed_text == expected_output

    def test_stemming_empty_string(self):
        # ARRANGE
        source_string = ""

        # ACT
        lemmatized_text = TextModifier.apply_stemming(source_string)

        # ASSERT
        expected_output = ""

        assert lemmatized_text == expected_output