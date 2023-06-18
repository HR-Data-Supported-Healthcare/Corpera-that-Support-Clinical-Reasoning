import re
from data_classes.paragraph import Paragraph

class ParagraphModifier():
    @staticmethod
    def remove_headings(paragraph_list: list[Paragraph]) -> tuple:
        """
        Removes headings from the paragraph list.

        Args:
            paragraph_list (list[Paragraph]): List of paragraphs.

        Returns:
            tuple: A tuple containing the list of kept paragraphs and the list of removed paragraphs.
        """
        print("Removing headings")
        removed_paragraphs = []
        kept_paragraphs = []
        for paragraph in paragraph_list: 
            paragraph_style: str = paragraph.style.name.lower()
            
            # Remove table of contents
            if paragraph.text.lower().startswith("inhoudsopgave") or paragraph_style == "tocheading":
                # i = remove_toc_headings(i)
                pass

            if not paragraph_style.startswith("heading") and not paragraph_style.startswith("kop"):
                kept_paragraphs.append(paragraph)
            else:
                print("Removing paragraph: title or heading")
                removed_paragraphs.append(paragraph)

        return kept_paragraphs, removed_paragraphs  

    @staticmethod
    def remove_title(paragraph_list: list[dict]) -> tuple:
        """
        Removes title and contact information from the document.

        Args:
            paragraph_list (list[dict]): List of paragraphs.

        Returns:
            tuple: A tuple containing the list of kept paragraphs and the list of removed paragraphs.
        """
        removed_paragraphs = []
        kept_paragraphs = []
        for paragraph in paragraph_list: 
            paragraph_style: str = paragraph.style.name.lower()
            
            # Remove Titlepage
            # TODO: Use a more robust regex for detecting contactgegevens paragraphs (if they have a specific structure).
            if paragraph_style.startswith("title") or paragraph_style.startswith("contactgegevens") or paragraph.text.lower().startswith("ondergetekende"):
                print("Removing paragraph: title or heading")
                removed_paragraph_dict = {"text" : paragraph.text, "style" : paragraph.style.name}
                removed_paragraphs.append(removed_paragraph_dict)
            else:
                kept_paragraphs.append(paragraph)
        return kept_paragraphs, removed_paragraphs  

    @staticmethod
    def remove_bibliography(paragraph_list: list[dict]) -> tuple:
        """
        Removes bibliography and appendix from the document.

        Args:
            paragraph_list (list[dict]): List of paragraphs.

        Returns:
            tuple: A tuple containing the list of kept paragraphs and the list of removed paragraphs.
        """
        # Remove source list
        removed_paragraphs = []
        kept_paragraphs = []
        for i, paragraph in enumerate(paragraph_list): 
            paragraph_style: str = paragraph.style.name.lower()
            paragraph_text: str = paragraph.text.lower()

            # Try to catch a bib paragraph, can just remove all paragraphs afterwards.
            if "bibliography" in paragraph_style or paragraph_text.startswith("literatuurlijst") or "geraadpleegd op " in paragraph_text:
                # Removing complete bibliography + appendix
                removed_paragraph_list = [{"text": p.text, "style" : p.style.name} for p in paragraph_list[i:]]
                removed_paragraphs.extend(removed_paragraph_list)
                break
            else:
                kept_paragraphs.append(paragraph)

        return kept_paragraphs, removed_paragraphs 
    
    @staticmethod
    def remove_tables_figures(paragraph_list: list[dict]) -> tuple:
        """
        Removes text explaining tables and figures from corpora (e.g: "Figuur 1.1: This is a figure").

        Args:
            paragraph_list (list[dict]): List of paragraphs.

        Returns:
            tuple: A tuple containing the list of kept paragraphs and the list of removed paragraphs.
        """
        # Remove source list
        removed_paragraphs = []
        kept_paragraphs = []
        for i, paragraph in enumerate(paragraph_list): 
            paragraph_text: str = paragraph.text.lower()
            # TODO: Handle cases like "Figuur 2A", "Figuur/tabel romeinse cijfering", etc.
            if re.match("^(figuur|tabel)\s[1-9](\.([1-9]|[1-9][1-9])(:|\.)|(:|\.)).*$", paragraph_text):
                print("Removing table or figure")
                removed_paragraph_dict = {"text" : paragraph.text , "style" : paragraph.style.name }
                removed_paragraphs.append(removed_paragraph_dict)
            else:
                kept_paragraphs.append(paragraph)

        return kept_paragraphs, removed_paragraphs
