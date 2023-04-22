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
        # self._load(dest_dir, transformed_data)

    def _transform(self, data: list[Document], flag_dict: dict):
        """ TODO: Docstring """
        corpora_total = {}
        corpora_total["config"] = flag_dict
        removed_paragraphs = []
        for current_doc, filename in data:
            current_doc_corpora : list[dict] = []
            doc_paragraphs = current_doc.paragraphs
            #headings should be removed separately (different paragraphs to remove together)
            if flag_dict["paragraph_filters"]["headings"]:
                corpora_with_headings_removed, removed_headings = ParagraphModifier.remove_headings(doc_paragraphs)   
                doc_paragraphs = corpora_with_headings_removed
                removed_paragraphs.extend(removed_headings)
            current_doc_corpora.extend(self.__transform_paragraphs_from_doc(doc_paragraphs, flag_dict))
            corpora_total[filename] = current_doc_corpora
        return corpora_total
            
    def __transform_paragraphs_from_doc(self, doc_paragraphs, flag_dict: dict) -> list[dict]:
        """TODO: Docstring"""
        total_doc_corpora = []
        for paragraph in doc_paragraphs:
            #For each paragraph, check the flag dictionary
            total_doc_corpora.append({})
            total_doc_corpora[-1]["text"] = paragraph.text
            total_doc_corpora[-1]["style"] = paragraph.style.name
            
            # Remove empty paragraphs
            if paragraph.text == "" or paragraph.text == "\n":
                del total_doc_corpora[-1]
                continue

            if flag_dict["text_transformations"]["stop_words"]: 
                print("removing stop words")
                with open('stopwords.json', 'r') as file:
                    stopwords = loads(file.read())  # list of dutch stopwords
                total_doc_corpora[-1]["text"] = TextModifier.remove_stop_words(total_doc_corpora[-1]["text"], stopwords)

            if flag_dict["text_transformations"]["lemmatization"]:
                print("applying lemmatization")
                total_doc_corpora[-1]["text"] = TextModifier.apply_lemmatization(total_doc_corpora[-1]["text"])

            if flag_dict["text_transformations"]["stemming"]:
                print("applying stemming")
                total_doc_corpora[-1]["text"] = TextModifier.apply_stemming(total_doc_corpora[-1]["text"])
        return total_doc_corpora

    def _load(self, dest_str: str, data):
        """
        TODO: Docstring
        """
        json_str = jsonpickle.encode(data)
        with open (dest_str, "w") as f:
            f.write(json_str)