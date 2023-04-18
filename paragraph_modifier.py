class ParagraphModifier():
    @staticmethod
    def lemmatisation(paragraph_text: str) -> str:
        pass

    @staticmethod
    def stemming(paragraph_text: str) -> str:
        pass

    @staticmethod
    def remove_heading(paragraph_text: dict) -> dict:
        pass

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