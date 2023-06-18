"""TODO: Docstring"""
from dataclasses import dataclass

@dataclass     
class ParagraphFlags():
     remove_title_page:         bool = True
     remove_headings:           bool = True
     remove_bibliography:       bool = True
     remove_tables_and_figures: bool = True

@dataclass
class TextFlags():
    remove_stop_words:      bool = True
    remove_punctuation:     bool = True
    apply_stemming:         bool = False
    apply_lemmatization:    bool = True

@dataclass
class CorporaGenerationFlags():
    #log_level: LogLevel TODO: Create LogLevel enum to be able to 
    create_preview: bool = False

@dataclass
class FlagContainer():
    paragraph_flags:    ParagraphFlags
    text_flags:         TextFlags
    #training_flags:     CorporaGenerationFlags