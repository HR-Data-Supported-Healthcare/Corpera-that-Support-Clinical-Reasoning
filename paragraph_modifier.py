import spacy;
from spacy.lang.nl.examples import sentences;

class ParagraphModifier():
    @staticmethod
    def lemmatisation(paragraph_text: str) -> str:
        nlp = spacy.load("nl_core_news_sm")
        doc = nlp(paragraph_text)
        modified_paragraph = paragraph_text
        for word in doc:
            if word.pos_ == "VERB":
                print(word, word.lemma_)
                modified_paragraph = modified_paragraph.replace(f"{word}", f"{word.lemma_}")
        return modified_paragraph

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
    def remove_stop_words(paragraph_text: str) -> str:
        from json import loads
        from string import punctuation

        # functions used to normalize words
        def remove_punctuation(chars):
            return chars.translate(str.maketrans('', '', punctuation))

        def to_lower(word):
            return str.lower(word)

        # read all words as a list, this list will be modified along the loop
        text = paragraph_text.split(' ')

        with open('stopwords.json', 'r') as file:
            stopwords = loads(file.read())  # list of dutch stopwords

        # the following loop directly removes a word from `text` if the word is found in the `stopwords` list
        for index, word in enumerate(text):
            # words must be normalized so that it can be matched with the stopwords list
            normalized_word = to_lower(remove_punctuation(word))

            if normalized_word in stopwords:
                del text[index]  # delete entry from `text` by index

        return ' '.join(text)
