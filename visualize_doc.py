from docx import Document
from docx.shared import RGBColor
from modifiers.paragraph_identifier import ParagraphIdentifier
from modifiers.text_modifier import TextModifier
from dataclasses import dataclass

@dataclass
class VisualizeFlags:
    visualize_stop_words: bool
    visualize_stemming: bool
    visualize_lemmatization: bool
    visualize_bibliography: bool
    visualize_table_figures: bool
    visualize_titlepage: bool
    visualize_headings: bool

@staticmethod
def visualize_text_modifications(paragraph_list: list[dict], vis_flags: VisualizeFlags, stop_words_list: list[str] = []) -> None:
    """TODO: Docstring
    if vis_flags.lemmatization and vis_flags.stemming both true, only does lemmatization
    """
    
    #colors for each paragraph to differentiate
    stop_words_color = RGBColor(255, 0, 0) #Red
    headings_color = RGBColor(0, 0, 255) #Blue
    titlepage_color = RGBColor(179, 46, 161) #Purple
    bibliography_color = RGBColor(213, 165, 68) #Brown
    table_figures_color = RGBColor(102, 0, 51) #Dark purple
    visualized_document = Document()

    if vis_flags.visualize_lemmatization:
        stop_words_list = [TextModifier.apply_lemmatization(w) for w in stop_words_list]
        
    elif vis_flags.visualize_stemming:
        stop_words_list = [TextModifier.apply_stemming(w) for w in stop_words_list]
    #remove duplicate entries in stop word list
    stop_words_list = list(set(stop_words_list))
    for paragraph in paragraph_list: 
        paragraph_text = paragraph.text
        main_color = RGBColor(0, 0, 0) #If paragraph does not conform to any removal specifications, make it black
        if ParagraphIdentifier.is_paragraph_heading(paragraph.style.name) and vis_flags.visualize_headings:
            main_color = headings_color
        elif ParagraphIdentifier.is_paragraph_title(paragraph.style.name, paragraph.text) and vis_flags.visualize_titlepage:
            main_color = titlepage_color
        elif ParagraphIdentifier.is_paragraph_table_or_figure(paragraph.text) and vis_flags.visualize_table_figures:
            main_color = table_figures_color
        elif ParagraphIdentifier.is_paragraph_bibliography(paragraph.style.name, paragraph.text) and vis_flags.visualize_bibliography:
            main_color = bibliography_color

        if vis_flags.visualize_lemmatization:
            paragraph_text = TextModifier.apply_lemmatization(paragraph_text)
        elif vis_flags.visualize_stemming:
            paragraph_text = TextModifier.apply_stemming(paragraph_text)
        new_p = visualized_document.add_paragraph()
        if len(stop_words_list) > 0:
            color_paragraph(paragraph_text , new_p, main_color, stop_words_list, stop_words_color)
        else:
            color_paragraph(paragraph_text , new_p, main_color)

    #TODO: return document and save elsewhere
    visualized_document.save('new_test.docx')
    return

def color_paragraph(text: str, paragraph, main_color: RGBColor, stop_words_list: list[str]= None, stop_words_color: RGBColor = None):
    if stop_words_list is None:
        run = paragraph.add_run(text)
        run.font.color.rgb = main_color
        return paragraph
    
    split_text = text.split()
    current_run_text : str = ""
    for word in split_text:
        if word.lower() not in stop_words_list: 
            current_run_text = current_run_text + word + " "
        else:
            if len(current_run_text) > 0:
                main_run = paragraph.add_run(current_run_text)
                main_run.font.color.rgb = main_color
                current_run_text = ""
            stop_words_run = paragraph.add_run(word + " ")
            stop_words_run.font.color.rgb = stop_words_color
    #Add the remaining words to paragraph
    remaining_run = paragraph.add_run(current_run_text)
    remaining_run.font.color.rgb = main_color
    return paragraph

"""
def color_stop_words(text: str, stop_words: list[str], paragraph, color: RGBColor = RGBColor(255, 0, 0)):

    TODO: DocString
    Returns doxc `Document` paragraph object

    
    split_text = text.split()
    current_run_text : str = ""
    for word in split_text:
        if word.lower() not in stop_words: 
            current_run_text = current_run_text + word + " "
        else:
            if len(current_run_text) > 0:
                paragraph.add_run(current_run_text)
                current_run_text = ""
            run = paragraph.add_run(word + " ")
            run.font.color.rgb = color
    #Add the remaining words to paragraph
    paragraph.add_run(current_run_text)
    return paragraph
"""

#Constants
DATA_DIR = "./data/BL_casereport1.docx"


if __name__ == "__main__":
    sw = [
    "aan",
    "af",
    "al",
    "alle",
    "alleen",
    "alles",
    "als",
    "alsmede",
    "ander",
    "andere",
    "anders",
    "ben",
    "bij",
    "bijna",
    "bijv",
    "bijvoorbeeld",
    "binnen",
    "boven",
    "bovendien",
    "bv",
    "daar",
    "daaraan",
    "daarbij",
    "daarbuiten",
    "daardoor",
    "daarin",
    "daarna",
    "daarnaast",
    "daarom",
    "daaronder",
    "daarop",
    "daarover",
    "daartoe",
    "daaruit",
    "daarvan",
    "daarvoor",
    "dan",
    "dat",
    "de",
    "der",
    "deze",
    "die",
    "dit",
    "door",
    "doordat",
    "dus",
    "dwz",
    "echter",
    "een",
    "eens",
    "eerst",
    "en",
    "enz",
    "er",
    "ermee",
    "erg",
    "ergens",
    "ervan",
    "ervaring",
    "ervoor",
    "etc",
    "even",
    "evenals",
    "eveneens",
    "ge",
    "geen",
    "gehad",
    "geweest",
    "geworden",
    "had",
    "hadden",
    "heb",
    "hebben",
    "hebt",
    "heden",
    "heeft",
    "hem",
    "hen",
    "het",
    "hier",
    "hieraan",
    "hierbij",
    "hierdoor",
    "hierin",
    "hiermee",
    "hierna",
    "hieronder",
    "hierop",
    "hiertoe",
    "hieruit",
    "hiervan",
    "hiervoor",
    "hij",
    "hoe",
    "hoewel",
    "hun",
    "ik",
    "in",
    "indien",
    "is",
    "ja",
    "je",
    "jij",
    "jullie",
    "kan",
    "kon",
    "konden",
    "kunt",
    "kunnen",
    "maar",
    "maw",
    "me",
    "mee",
    "men",
    "met",
    "middels",
    "mijn",
    "misschien",
    "mits",
    "na",
    "naar",
    "naast",
    "nadat",
    "nee",
    "net",
    "niet",
    "niets",
    "nl",
    "nog",
    "nogal",
    "nou",
    "nu",
    "of",
    "om",
    "omdat",
    "ondermeer",
    "ons",
    "onze",
    "ook",
    "op",
    "over",
    "overig",
    "overige",
    "overigens",
    "reeds",
    "sinds",
    "slechts",
    "soms",
    "tbv",
    "te",
    "tegen",
    "ten",
    "tenzij",
    "ter",
    "terug",
    "terwijl",
    "tevens",
    "tijdens",
    "toch",
    "toe",
    "toen",
    "tot",
    "totdat",
    "tussen",
    "uit",
    "uw",
    "vaak",
    "van",
    "vanaf",
    "vandaar",
    "vanuit",
    "vanwege",
    "vervolgens",
    "volgens",
    "voor",
    "vooraf",
    "vooral",
    "voordat",
    "voorheen",
    "voornamelijk",
    "waar",
    "waaraan",
    "waarbij",
    "waardoor",
    "waarin",
    "waarmee",
    "waarna",
    "waarom",
    "waarop",
    "waaronder",
    "waaruit",
    "waarvan",
    "waarvoor",
    "wanneer",
    "want",
    "waren",
    "was",
    "wat",
    "we",
    "weer",
    "wel",
    "welk",
    "welke",
    "wellicht",
    "werd",
    "werden",
    "wie",
    "wij",
    "worden",
    "wordt",
    "zal",
    "ze",
    "zeer",
    "zelf",
    "zelfs",
    "zich",
    "zij",
    "zijn",
    "zo",
    "zoals",
    "zodat",
    "zonder",
    "zowel",
    "zou",
    "zouden",
    "zult",
    "zullen"
]
    flags = VisualizeFlags(True, False, True, True, True, True, True)
    doc = Document(DATA_DIR)
    visualize_text_modifications(doc.paragraphs, flags, sw )