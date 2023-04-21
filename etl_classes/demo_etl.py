import jsonpickle
from .base_etl_class import BaseETL

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