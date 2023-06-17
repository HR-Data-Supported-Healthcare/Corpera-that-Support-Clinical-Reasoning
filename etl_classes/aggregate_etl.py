from docx import Document
from docxcompose.composer import Composer
from .base_etl_class import BaseETL

class AggregateETL(BaseETL):
    """
    Class representing the AggregateETL (Extract, Transform, Load) process.

    Args:
        data_dir (str): The directory containing the input data.
        dest_dir (str): The directory where the output will be saved.
    """
    def __init__(self, data_dir: str, dest_dir: str):
        super().__init__(data_dir, dest_dir)

    def _transform(self, data: list[Document]) -> Composer:
        """
        Transforms the input data by combining multiple Document objects into a single Composer object.

        Args:
            data (list[Document]): The list of Document objects to be combined.

        Returns:
            Composer: The combined Composer object.
        """
        docx_files = data
        number_of_sections = len(docx_files)
        master = data[0][0]
        composer = Composer(master)
        for i in range(1, number_of_sections):
            doc_temp = docx_files[i][0]
            composer.append(doc_temp)
        return composer

    def _load(self, dest_str: str, data: Composer) -> None:
        """
        Saves the transformed data (Composer object) to the specified destination.

        Args:
            dest_str (str): The path to save the transformed data.
            data (Composer): The transformed data to be saved.

        Returns:
            None
        """
        data.save(dest_str)
