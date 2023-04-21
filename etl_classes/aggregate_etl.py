from docx import Document
from docxcompose.composer import Composer
from .base_etl_class import BaseETL

class AggregateETL(BaseETL):
    """ TODO: DOCSTRING """
    def __init__(self, data_dir: str, dest_dir: str):
        super().__init__(data_dir, dest_dir)

    def _transform(self, data: list[Document]):
        """ TODO: DOCSTRING """
        #reasignment for name clarity
        docx_files = data 
        number_of_sections=len(docx_files)
        #TODO: Check len for out of range
        master = data[0][0] #TODO: Might want to select master file manually using param
        composer = Composer(master)
        for i in range(1, number_of_sections):
            doc_temp = docx_files[i][0]
            composer.append(doc_temp)
        #composer.save("combined_file.docx")
        return composer

    def _load(self, dest_str: str, data: Composer):
        """ TODO: Docstring """
        data.save(dest_str)