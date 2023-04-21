class ParagraphModifier():
    @staticmethod
    def remove_headings(paragraph_list: list[dict]) -> tuple:
        """
        removes headings from given paragraphs, returns the list of remaining paragraphs and a list which contained the removed sections 
        TODO: proper docstring
        """
        #TODO: Perhaps want these headings to be variable params
        #TODO: add more headings to the list
        #heading_list = ["heading 1", "heading 2", "heading 3", "heading 4", "heading 5", "heading 6", "heading 7", "heading 8", "heading 9","title" ]
        """
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
        """
        print("removing headings")
        removed_paragraphs = []
        kept_paragraphs = []
        for paragraph in paragraph_list: 
            paragraph_style: str = paragraph.style.name.lower()
            # Remove table of contents
            if paragraph.text.lower().startswith("inhoudsopgave") or paragraph_style == "tocheading":
                #i = remove_toc_headings(i)
                pass

            # Remove Titlepage
            #TODO: is title a heading?
            if not paragraph_style.startswith("title") and not paragraph_style.startswith("heading") and not paragraph_style.startswith("kop"):
                print("Removing paragraph: heading")
                kept_paragraphs.append(paragraph)
            else:
                removed_paragraph_dict = {"text" : paragraph.text , "style" : paragraph.style.name }
                removed_paragraphs.append(removed_paragraph_dict)

        return kept_paragraphs, removed_paragraphs  
                
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