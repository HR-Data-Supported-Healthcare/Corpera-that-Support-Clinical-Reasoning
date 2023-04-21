from modifiers.text_modifier import TextModifier

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

source_string = "Doordat deze ziekte lastig was vast te stellen zorgde dit voor veel \
    vragen en spanningen bij de patiënt en het zorgpersoneel en ook bij mij. \
    Ik vond het lastig om te zien dat iemand achteruit blijft gaan, maar dat het zoeken is naar de oorzaak."

expected_output = "Doordat ziekte lastig vast stellen zorgde veel \
    vragen en spanningen patiënt en zorgpersoneel en mij. \
    Ik vond lastig zien iemand achteruit blijft gaan, zoeken is naar oorzaak."


def test_remove_stop_words_from_dutch_text():
    assert TextModifier.remove_stop_words(
        source_string, stopwords_list) == expected_output
