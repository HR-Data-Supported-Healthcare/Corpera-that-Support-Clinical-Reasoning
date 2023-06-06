from docx import Document
import jsonpickle
from modifiers.paragraph_modifier import ParagraphModifier
from modifiers.text_modifier import TextModifier
from .base_etl_class import BaseETL
from json import loads

class DynamicETL(BaseETL):
    """ TODO: Docstring """
    def __init__(self, data_dir: str, dest_dir: str, flag_dict: dict):
        self._execute_etl(data_dir, dest_dir, flag_dict)

    def _execute_etl(self, data_dir: str, dest_dir: str, flag_dict: dict) -> None:
        extracted_data = self._extract(data_dir)
        transformed_data = self._transform(extracted_data, flag_dict)
        self._load(dest_dir, transformed_data)

    def _transform(self, data: list[Document], flag_dict: dict):
        """ TODO: Docstring """
        corpora_total = {}
        corpora_total["config"] = flag_dict
        corpora_total["documents"] = []

        removed_paragraphs = [] #TODO: Implement paragraphs
        for current_doc, filename in data:
            current_doc_obj = {"filename" : filename}
            current_doc_corpora : list[dict] = []
            kept_paragraphs, _ = self.__remove_paragraphs_from_doc(current_doc.paragraphs, flag_dict["paragraph_filters"])
            current_doc_corpora.extend(self.__transform_paragraphs_from_doc(kept_paragraphs, flag_dict["text_transformations"])) #TODO: Only sent flag_dict["text-filters"]
            current_doc_obj["corpora"] = current_doc_corpora
            corpora_total["documents"].append(current_doc_obj)

        return corpora_total

    def __remove_paragraphs_from_doc(self, doc_paragraphs, flag_dict:dict) -> tuple:
        removed_paragraphs = []
        if flag_dict["titlepage"]:
            print("removing titlepage")
            corpora_with_headings_removed, removed_headings = ParagraphModifier.remove_title(doc_paragraphs)   
            doc_paragraphs = corpora_with_headings_removed
            removed_paragraphs.extend(removed_headings)

        #remove bib before bab
        if flag_dict["bibliography"]:
            print("removing bib")
            corpora_with_headings_removed, removed_headings = ParagraphModifier.remove_bibliography(doc_paragraphs)   
            doc_paragraphs = corpora_with_headings_removed
            removed_paragraphs.extend(removed_headings)
        #headings should be removed separately (different paragraphs to remove together)

        if flag_dict["headings"]:
            corpora_with_headings_removed, removed_headings = ParagraphModifier.remove_headings(doc_paragraphs)   
            doc_paragraphs = corpora_with_headings_removed
            removed_paragraphs.extend(removed_headings)

        if flag_dict["tables_and_figures"]:
            corpora_with_headings_removed, removed_headings = ParagraphModifier.remove_tables_figures(doc_paragraphs)   
            doc_paragraphs = corpora_with_headings_removed
            removed_paragraphs.extend(removed_headings)

        return doc_paragraphs, removed_paragraphs

    def __transform_paragraphs_from_doc(self, doc_paragraphs, flag_dict: dict) -> list[dict]:
        """TODO: Docstring"""
        total_doc_corpora = []
        for paragraph in doc_paragraphs: 
            # Remove empty paragraphs
            if paragraph.text == "" or paragraph.text == " " or paragraph.text == "\n":
                continue

            #TODO: Should not do this here
            #Remove paragraphs containing only 1 or 2 words
            if len(paragraph.text.split()) < 3:
                continue

            current_paragraph_obj = {"text" : paragraph.text.strip(), "style": paragraph.style.name}
            #For each paragraph, check the flag dictionary
            if flag_dict["stop_words"]: 
                print("removing stop words")
                with open('stopwords.json', 'r') as file:
                    stopwords = loads(file.read())  # list of dutch stopwords
                current_paragraph_obj["text"] = TextModifier.remove_stop_words(current_paragraph_obj["text"], stopwords)

            if flag_dict["lemmatization"]:
                print("applying lemmatization")
                current_paragraph_obj["text"] = TextModifier.apply_lemmatization(current_paragraph_obj["text"])

            if flag_dict["stemming"]:
                print("applying stemming")
                current_paragraph_obj["text"] = TextModifier.apply_stemming(current_paragraph_obj["text"])
            total_doc_corpora.append(current_paragraph_obj)
        return total_doc_corpora

    def _load(self, dest_str: str, data):
        """
        TODO: Docstring
        """
        json_str = jsonpickle.encode(data)
        with open (dest_str, "w") as f:
            f.write(json_str)