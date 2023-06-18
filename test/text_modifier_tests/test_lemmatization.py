import unittest
from modifiers.text_modifier import TextModifier


class TestLemmatization(unittest.TestCase):
    def test_lemmatize(self):
        # ARRANGE
        source_string = "Vanochtend ben ik vroeg opgestaan en heb ik een lekkere kop koffie gezet. Vervolgens heb ik mijn tanden gepoetst en ben ik naar buiten gegaan om een stuk te gaan hardlopen. Na het rennen heb ik gedoucht en me aangekleed."

        # ACT
        lemmatized_text = TextModifier.apply_lemmatization(source_string)

        # ASSERT
        expected_output = "vanochtend zijn ik vroeg opgestaan en hebben ik een lekker kop koffie zetten. vervolgens hebben ik mijn tand poetsen en zijn ik naar buiten gaan om een stuk te gaan hardlopen. na het rennen hebben ik douchen en me aangekleed."

        assert lemmatized_text == expected_output

    def test_lemmatize_empty_string(self):
        # ARRANGE
        source_string = ""

        # ACT
        lemmatized_text = TextModifier.apply_lemmatization(source_string)

        # ASSERT
        expected_output = ""

        assert lemmatized_text == expected_output
