from abc import ABC, abstractmethod
from docx import Document
import os

class BaseETL(ABC):
    """
    Abstract base class for ETL (Extract, Transform, Load) subclasses.
    """
    @abstractmethod
    def __init__(self, data_dir: str, dest_dir: str):
        """
        Initializes the BaseETL instance.

        Args:
            data_dir (str): The directory containing the input data.
            dest_dir (str): The directory where the output will be saved.
        """
        self._execute_etl(data_dir, dest_dir)

    def _execute_etl(self, data_dir: str, dest_dir: str) -> None:
        """
        Executes the ETL process.

        Args:
            data_dir (str): The directory containing the input data.
            dest_dir (str): The directory where the output will be saved.

        Returns:
            None
        """
        extracted_data = self._extract(data_dir)

        if len(extracted_data) == 0:
            exit(f"Exiting ETL. There are no files to transform. Please make sure there is available data in {data_dir}")

        transformed_data = self._transform(extracted_data)
        self._load(dest_dir, transformed_data)

    def _extract(self, data_dir: str) -> list[Document]:
        """
        Extracts data from the specified directory.

        Args:
            data_dir (str): The directory containing the input data.

        Returns:
            list[Document]: The extracted data as a list of Document objects.
        """
        doc_list: list[Document] = []
        for filename in os.listdir(data_dir):
            if filename.endswith('.docx'):
                print(f"[EXTRACT] Extracted docx file '{filename}'")
                doc_list.append((Document(f"{data_dir}/{filename}"), filename))

        return doc_list

    @abstractmethod
    def _transform(self, data) -> object:
        """
        Transforms the extracted data.

        Args:
            data: The extracted data.

        Returns:
            object: The transformed data.
        """
        pass

    @abstractmethod
    def _load(self, dest_str: str, data) -> None:
        """
        Loads the transformed data.

        Args:
            dest_str (str): The path to save the transformed data.
            data: The transformed data.

        Returns:
            None
        """
        pass
