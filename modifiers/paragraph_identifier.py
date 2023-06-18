"""TODO: Docstring"""
import re

class ParagraphIdentifier():
    @staticmethod
    def is_paragraph_heading(paragraph_style_name: str = None) -> bool:
        """
        Checks if given paragraph is heading. paragraph_style optional
        returns true if heading, else false
        TODO: proper docstring
        """
        if paragraph_style_name.lower().startswith("heading") or paragraph_style_name.lower().startswith("kop"):
            return True
        return False
    
    @staticmethod  
    def is_paragraph_title(paragraph_style_name: str, paragraph_text: str) -> bool:
        """TODO: Docstring"""
        if paragraph_style_name.lower().startswith("title") or paragraph_style_name.lower().startswith("contactgegevens"):
            return True
        if paragraph_text.lower().startswith("ondergetekende"):
            return True
        return False
    
    @staticmethod
    def is_paragraph_bibliography(paragraph_style_name: str, paragraph_text: str) -> bool:
        """TODO: Docstring"""
        if "bibliography" in paragraph_style_name.lower():
            return True
        #TODO: insecure criteria "geraadpleegd op"
        if paragraph_text.lower().startswith("literatuurlijst") or "geraadpleegd op " in paragraph_text.lower():
            return True
        return False

    @staticmethod 
    def is_paragraph_table_or_figure(paragraph_text: str) -> bool:
        """TODO: Docstring"""
        if re.match("^(figuur|tabel)\s[1-9](\.([1-9]|[1-9][1-9])(:|\.)|(:|\.)).*$", paragraph_text.lower()):
            return True
        return False