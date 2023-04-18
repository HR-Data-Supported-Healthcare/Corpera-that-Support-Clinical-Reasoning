from docx import Document
import os
import jsonpickle
from docxcompose.composer import Composer
from paragraph_modifier import ParagraphModifier
import os

#TODO: Abstract class with abc lib? Does not make much sense with static methods
#TODO: Perhaps classes can be stored in seperate files for less total imports
#TODO: Revise class structure idea, might not be necessary

class AbstractETL():
    """
    Class which can be used for ETL subclasses
    """
    @staticmethod
    def extract(data_dir)-> list[Document]:
        """ TODO: Docstring """
        doc_list : list [Document] = []
        for filename in os.listdir(data_dir):
            doc_list.append((Document(f"{data_dir}/{filename}"), filename))
        return doc_list

    #@abc.abstractmethod
    @staticmethod
    def transform(data):
        """ TODO: Docstring """
        pass

    #@abc.abstractmethod
    @staticmethod
    def load(dest_str: str, data):
        """ TODO: Docstring """
        pass


class DemoETL(AbstractETL):
    """ TODO: Docstring """
    def transform(data):
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
    
    @staticmethod
    def load(dest_str: str, data):
        """
        TODO: Docstring
        """
        json_str = jsonpickle.encode(data)
        with open (dest_str, "w") as f:
            f.write(json_str)



class DynamicETL(AbstractETL):
    """ TODO: Docstring """
    def transform(data, flag_dict={}, ):
        """ TODO: Docstring """

        for key in flag_dict:
            if flag_dict[key] is True and key == "stop_words":
                ParagraphModifier.remove_stop_words()
            pass


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

    @staticmethod
    def load(dest_str: str, data):
        """
        TODO: Docstring
        """
        json_str = jsonpickle.encode(data)
        with open (dest_str, "w") as f:
            f.write(json_str)
"""


"""


class AggregateETL(AbstractETL):
    """ TODO: DOCSTRING """
    @staticmethod
    def transform(data: list[Document]):
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

    @staticmethod
    def load(dest_str: str, data: Composer):
        """ TODO: Docstring """
        data.save(dest_str)