"""
The front-end file of the natural language processing program.
"""

import backend


class Interface:
    """
    This parent class is an API
    for the natural language processing module.
    Calls: 'backend.py'
    Called in: 'main.py'

    Methods:
    file_open(): opens and reads the text file
                 with the text to process
    """

    def __init__(self, file):
        """
        The initial method of the class.

        Parameter:
        :param file(str): complete path to the text file

        Initialized attribute:
        self.text(str): the text of the opened text file
        """
        self.file = file
        self.text = ""

    def __str__(self):
        """
        The method provides a brief prompt
        about the functions of this class.

        :return(str): the prompt
        """
        return ("This class is a graphical interface "
                "for a natural language processing code.")

    def file_open(self):
        """
        This methods opens and reads the text file.

        :return self.text(str): the text of the opened text file
        """
        doc = open(self.file)
        self.text = doc.read()
        doc.close()
        return self.text


class MorphInterface(Interface):
    """
    This child class executes
    morphological processing of the text.

    Methods:
    get_w_tokens(): calls the word-tokenizing method
                    from the backend-module
    get_s_tokens(): calls the sentence-tokenizing method
                    from the backend-module
    get_stop_words(): calls the stop-word excluding method
                      from the backend-module
    """

    def __str__(self):
        """
        The method provides a brief prompt
        about the functions of this class.

        :return(str): the prompt
        """
        return ("This class provides "
                "morphological processing of the text.")

    def get_w_tokens(self):
        """
        This method calls for word-tokenizing.

        :return (list): tokenized words from the text
        """
        return backend.TokensStopwords.w_tokenizer(self.text)

    def get_s_tokens(self):
        """
        This method calls for sentence-tokenizing.

        :return (list): tokenized sentences from the text
        """
        return backend.TokensStopwords.s_tokenizer(self.text)

    def get_stop_words(self):
        """
        This method calls for the removal of stop-words.

        :return (list): tokenized words from the text
                        without stop-words
        """
        return backend.TokensStopwords.stats_qualifier(self.text)


class SemanticInterface(Interface):
    """
    This child class executes
    semantic processing of the text.

    Methods:
    get_lemmatizing(): calls the lemmatizing method
                       from the backend-module
    get_stemming(): calls the stemming method
                    from the backend-module
    get_tags(): calls the tagging method
                   from the backend-module
    """

    def __str__(self):
        """
        The method provides a brief prompt
        about the functions of this class.

        :return(str): the prompt
        """
        return ("This class provides "
                "semantic processing of the text.")

    def get_lemmatizing(self):
        """
        This method calls for word lemmatizing.

        :return (dict): pairs of token(key) - lemmatized word(value)
        """
        return backend.SemanticProcessing.lemmatizing(self.text)

    def get_stemming(self):
        """
        This method calls for word stemming.

        :return (dict): pairs of token(key) - stemmed word(value)
        """
        return backend.SemanticProcessing.stemming(self.text)

    def get_tags(self):
        """
        This method calls for word tagging.

        :return (list): a list of paired tuples of token - tag
        """
        return backend.SemanticProcessing.tagging(self.text)


class SystemInterface(Interface):
    """
    This child class executes
    classification and analysis of the text.

    Methods:
    get_classifying(): calls the frequency distribution method
                       from the backend-module
    get_analysis(): calls the text analysis method
                    from the backend-module
    """

    def __str__(self):
        """
        The method provides a brief prompt
        about the functions of this class.

        :return(str): the prompt
        """
        return ("This class operates the text "
                "and outputs most frequent tokens;\n"
                "searches for definitions, synonyms "
                "and antonyms of the input token.")

    def get_classifying(self):
        """
        This method calls for classification.

        :return nltk.probability object: class object for tokens,
                                         distributed by frequency
        """
        return backend.Systematization.classifying(self.text)

    def get_analysis(self):
        """
        This method calls for lexical analysis.

        :return (list): synset items of synonyms for a token
        """
        return backend.Systematization.analyzing(self.text)
