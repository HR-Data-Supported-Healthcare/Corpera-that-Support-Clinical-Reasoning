from modifiers.text_modifier import TextModifier

source_string = "Vanochtend ben ik vroeg opgestaan en heb ik een lekkere kop koffie gezet. \
    Vervolgens heb ik mijn tanden gepoetst en ben ik naar buiten gegaan om een stuk te gaan hardlopen. \
    Na het rennen heb ik gedoucht en me aangekleed."

expected_output = "Vanochtend ben ik vragen opgestaan en heb ik een lekkere kop koffie zetten. \
    Vervolgens heb ik mijn tanden poetsen en ben ik naar buiten gaan om een stuk te gaan hardlopen. \
    Na het rennen heb ik douchten en me aangekleed."


def test_lemmatize_dutch_text():
    assert TextModifier.apply_lemmatization(source_string) == expected_output
