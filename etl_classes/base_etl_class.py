from abc import ABC, abstractmethod
from docx import Document
import os

class BaseETL(ABC):
    """
    Class which can be used for ETL subclasses
    """
    @abstractmethod
    def __init__(self, data_dir: str, dest_dir: str):
        self._execute_etl(data_dir, dest_dir)

    def _execute_etl(self, data_dir: str, dest_dir: str) -> None:
        extracted_data = self._extract(data_dir)
        transformed_data = self._transform(extracted_data)
        self._load(dest_dir, transformed_data)

    def _extract(self, data_dir: str)-> list[Document]:
        """ TODO: Docstring """
        doc_list : list [Document] = []
        for filename in os.listdir(data_dir):
            doc_list.append((Document(f"{data_dir}/{filename}"), filename))
        return doc_list
    
    @abstractmethod
    def _transform(self, data) -> object:
        """ TODO: Docstring """
        pass

    @abstractmethod
    def _load(dest_str: str, data) -> None:
        """ TODO: Docstring """
        pass