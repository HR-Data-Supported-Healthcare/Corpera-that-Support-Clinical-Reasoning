from docx import Document
import jsonpickle
from docxcompose.composer import Composer
from paragraph_modifier import ParagraphModifier
from base_etl_class import BaseETL

#TODO: Perhaps classes can be stored in seperate files for less total imports
#TODO: Revise class structure idea, might not be necessary

class DemoETL(BaseETL):
    """ TODO: Docstring """
    def __init__(self, data_dir: str, dest_dir: str):
        super().__init__(data_dir, dest_dir)

    def _transform(self, data):
        """ TODO: Docstring """
        corpora_obj = {}
        for current_doc, filename in data:
            print(len(current_doc.paragraphs))
            corpora : list[list] = []
            i: int = 0
            while i < len(current_doc.paragraphs):
                #Remove Titlepage
                if current_doc.paragraphs[i].style.name.startswith("Title"):
                     print("Removing paragraph: Title")
                     pass
        
                #Remove table of contents heading + body
                elif current_doc.paragraphs[i].text.lower().startswith("inhoudsopgave") or current_doc.paragraphs[i].style.name == "TOCHeading":
                    print("Removing paragraph: toc")
                    #TODO: Perhaps table of contents is merged in one paragraph, should check
                    #Remove next paragraph too
                    i += 1

                #Remove paragraph headings
                elif current_doc.paragraphs[i].style.name.startswith("Heading"):
                     print("Removing paragraph: heading")
                     #TODO: Perhaps headings can be transformed instead -> may hold value
                     pass
                
                #Remove source list 
                elif "bibliography" in current_doc.paragraphs[i].style.name.lower() or current_doc.paragraphs[i].text.lower().startswith("literatuurlijst"):
                     print("Removing paragraph: source list")
                     pass
                
                #Remove table annotations
                elif False:
                     print("Removing paragraph: annotation")
                     #TODO
                     pass
                
                #Remove picture annotations
                elif False:
                     print("Removing paragraph: annotation")
                     #TODO
                     pass
                
                #Remove empty paragraphs
                elif current_doc.paragraphs[i].text == "":
                     print("Removing paragraph: empty paragraph") 
                     #TODO
                     pass
                
                else:
                    print("Adding text to corpora")
                    corpora.append([current_doc.paragraphs[i].text, []])
                i += 1
            corpora_obj[filename] = corpora
        return corpora_obj
    
    def _load(self, dest_str: str, data):
        """
        TODO: Docstring
        """
        json_str = jsonpickle.encode(data)
        with open (dest_str, "w") as f:
            f.write(json_str)

class DynamicETL(BaseETL):
    """ TODO: Docstring """
    def _transform(self, data: list[Document], flag_dict={}, ):
        """ TODO: Docstring """ #TODO: stemming and lemmatisation -> apply_stemming, apply_lemmatisation

        for paragraph in data:
            if flag_dict["stop_words"] is True:
                paragraph["text"] = ParagraphModifier.remove_stop_words(paragraph["text"])
            if flag_dict["lemmatisation"] is True:
                paragraph["text"] = ParagraphModifier.lemmatisation(paragraph["text"])
            if flag_dict["stemming"] is True:
                paragraph["text"] = ParagraphModifier.stemming(paragraph["text"])
            if flag_dict["heading"] is True:
                paragraph = ParagraphModifier.stemming(paragraph)

    def _load(dest_str: str, data):
        """
        TODO: Docstring
        """
        json_str = jsonpickle.encode(data)
        with open (dest_str, "w") as f:
            f.write(json_str)

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