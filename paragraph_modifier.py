class ParagraphModifier():
    @staticmethod
    def lemmatisation(paragraph_text: str) -> str:
        pass

    @staticmethod
    def stemming(paragraph_text: str) -> str:
        pass

    @staticmethod
    def remove_headings(paragraph_list: list[dict]) -> tuple:
        """
        removes headings from given paragraphs, returns the list of remaining paragraphs and a list which contained the removed sections 
        TODO: proper docstring
        """
        #TODO: Perhaps want these headings to be variable params
        #TODO: add more headings to the list
        #heading_list = ["heading 1", "heading 2", "heading 3", "heading 4", "heading 5", "heading 6", "heading 7", "heading 8", "heading 9","title" ]

        def remove_toc_headings(index):
            #TODO: Implement, Is this necessary? don't seem to get any TOCs except doc 10 (which has no styling)
            #TODO: TOC in separate function? just as bibliography
            print("Removing paragraph header: toc")
            j = index + 1
            found_next_section = False
            while not found_next_section:
                if paragraph_list[j].style.name == "TOCHeading":
                    pass
            return j
        print("removing headings")
        removed_paragraphs = []
        i = 0
        while i < len(paragraph_list):
            # Remove table of contents
            if paragraph_list[i].text.lower().startswith("inhoudsopgave") or paragraph_list[i].style.name == "TOCHeading":
                #i = remove_toc_headings(i)
                pass

            # Remove Titlepage
            #TODO: is title a heading?
            if paragraph_list[i].style.name.lower().startswith("title") or paragraph_list[i].style.name.startswith("heading") or paragraph_list[i].style.name.startswith("kop"):
                    print("Removing paragraph: heading")
                    removed_paragraph_dict = {"text" : paragraph_list[i].text , "style" : paragraph_list[i].style.name }
                    removed_paragraphs.append(removed_paragraph_dict)
                    del paragraph_list[i]
            i += 1
        return paragraph_list, removed_paragraphs  
                
    @staticmethod
    def remove_bibliography(paragraph_list: list[dict]) -> tuple:
        # Remove source list
        """
        if "bibliography" in current_doc.paragraphs[i].style.name.lower() or current_doc.paragraphs[i].text.lower().startswith("literatuurlijst"):
                print("Removing paragraph: source list")
                pass
        """
        removed_paragraphs = []
        i = 0
        while i < len(paragraph_list):
            # Remove table of contents
            if "bibliography" in paragraph_list[i].style.name.lower() or paragraph_list[i].text.lower().startswith("literatuurlijst"):
                print("Removing paragraph: source list")
                removed_paragraph_dict = {"text" : paragraph_list[i].text , "style" : paragraph_list[i].style.name }
                removed_paragraphs.append(removed_paragraph_dict)
                del paragraph_list[i]

        return paragraph_list, removed_paragraphs

    @staticmethod
    def remove_stop_words(stop_words: list[str], paragraph_text: str) -> str:
        #loop through text, remove words from text that are in stop_words list 
        #return text
        pass