import jsonpickle
from .base_etl_class import BaseETL

class DemoETL(BaseETL):
    """
    ETL subclass for the demo scenario.
    """
    def __init__(self, data_dir: str, dest_dir: str):
        """
        Initializes the DemoETL instance.

        Args:
            data_dir (str): The directory containing the input data.
            dest_dir (str): The directory where the output will be saved.
        """
        super().__init__(data_dir, dest_dir)

    def _transform(self, data):
        """
        Transforms the extracted data for the demo scenario.

        Args:
            data: The extracted data.

        Returns:
            dict: The transformed data as a dictionary.
        """
        corpora_obj = {}
        for current_doc, filename in data:
            print(len(current_doc.paragraphs))
            corpora: list[list] = []
            i: int = 0
            while i < len(current_doc.paragraphs):
                # Remove Titlepage
                if current_doc.paragraphs[i].style.name.startswith("Title"):
                     print("Removing paragraph: Title")
                     pass
        
                # Remove table of contents heading + body
                elif current_doc.paragraphs[i].text.lower().startswith("inhoudsopgave") or current_doc.paragraphs[i].style.name == "TOCHeading":
                    print("Removing paragraph: toc")
                    # TODO: Perhaps table of contents is merged in one paragraph, should check
                    # Remove next paragraph too
                    i += 1

                # Remove paragraph headings
                elif current_doc.paragraphs[i].style.name.startswith("Heading"):
                     print("Removing paragraph: heading")
                     # TODO: Perhaps headings can be transformed instead -> may hold value
                     pass
                
                # Remove source list 
                elif "bibliography" in current_doc.paragraphs[i].style.name.lower() or current_doc.paragraphs[i].text.lower().startswith("literatuurlijst"):
                     print("Removing paragraph: source list")
                     pass
                
                # Remove table annotations
                elif False:
                     print("Removing paragraph: annotation")
                     # TODO
                     pass
                
                # Remove picture annotations
                elif False:
                     print("Removing paragraph: annotation")
                     # TODO
                     pass
                
                # Remove empty paragraphs
                elif current_doc.paragraphs[i].text == "":
                     print("Removing paragraph: empty paragraph") 
                     # TODO
                     pass
                
                else:
                    print("Adding text to corpora")
                    corpora.append([current_doc.paragraphs[i].text, []])
                i += 1
            corpora_obj[filename] = corpora
        return corpora_obj
    
    def _load(self, dest_str: str, data):
        """
        Loads the transformed data into a JSON file.

        Args:
            dest_str (str): The path to save the transformed data.
            data: The transformed data.

        Returns:
            None
        """
        json_str = jsonpickle.encode(data)
        with open(dest_str, "w") as f:
            f.write(json_str)
