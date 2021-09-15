"""
The back-end file of the natural language processing program.
"""
import time
#
import nltk


class TokensStopwords:
    """
    This class executes such natural language-processing operations
    as word-tokenizing, sentence-tokenizing and removal of stop-words.

    Methods:
    w_tokenizer: executes tokenizing of words/punctuation marks
    s_tokenizer: executes tokenizing of sentences
    stats_qualifier: executes exclusion of stop-words
    """

    @staticmethod
    def w_tokenizer(text):
        """
        This method tokenizes words.

        :param text:(str)the text from the opened text file)
        :return tokens(list): tokenized words from the text
        """
        tokens = nltk.word_tokenize(text)
        print("\n".join(["".join(str(tokens[i:i + 25]))
                         for i in range(0, len(tokens), 25)]))
        print(f"TOTAL AMOUNT OF TOKENS: {len(tokens)}")

        return tokens

    @staticmethod
    def s_tokenizer(text):
        """
        This method tokenizes sentences.

        :param text:(str)the text from the opened text file)
        :return sentences(list): tokenized sentences from the text
        """
        sentences = nltk.sent_tokenize(text)
        numb = 1
        for sentence in sentences:
            print(f"{numb}. {sentence}")
            numb += 1
        print(f"TOTAL AMOUNT OF SENTENCES: {len(sentences)}")
        return sentences

    @staticmethod
    def stats_qualifier(text):
        """
        This method deletes stop-words.

        :param text:(str)the text from the opened text file)

        Introduced variables:
        tokens(list): tokenized words from the text
        stop_words(set): a set of English stop-words
        :return clear_text(list): tokenized words from the text
                                  without stop-words
        """
        tokens = nltk.word_tokenize(text)
        stop_words = set(nltk.corpus.stopwords.words("english"))
        clear_text = [token for token in tokens if token not in stop_words]
        print("\n".join(["".join(str(clear_text[i:i + 20]))
                         for i in range(0, len(clear_text), 20)]))
        print(f"TOTAL AMOUNT OF INFORMATIVE TOKENS: {len(clear_text)}")
        return clear_text


class SemanticProcessing:
    """
    This class executes such natural language-processing operations
    as lemmatizing, stemming and tagging.

    Methods:
    lemmatizing(): executes lemmatizing of the text
    stemming(): executes stemming of the text
    tagging(): executes tagging of the text
    """

    @staticmethod
    def lemmatizing(text):
        """
        This method lemmatizes tokens of the text.

        :param text:(str)the text from the opened text file)

        Introduced variables:
        lemm_list(list): the list of paired tokens - lemmatied words
        tokens(list): tokenized words from the text
        token(str): one token(item) from the list of tokens
        lemmatizer(obj): initialized instance
                         of the 'WordNetLemmatizer' class
        key, value(str): keys and values of the 'lemm_dict' dictionary

        :return lemm_dict(dict): pairs of token(key) - lemmatized word(value)
        """
        lemm_dict = {}
        lemm_list = []
        tokens = nltk.word_tokenize(text)
        lemmatizer = nltk.WordNetLemmatizer()
        # (The dictionary has unique key names.
        #  Hence, the number of keys
        #  falls behind the number of tokenized words.)
        # (Словари имеют уникальные названия ключения,
        #  вследствии чего после создания словаря
        #  колличество ключей уступает колличеству
        #  токенизированных слов.)
        for token in tokens:
            lemm_dict[token] = lemmatizer.lemmatize(token.lower())
        for key, value in lemm_dict.items():
            item = key + ": " + value
            lemm_list.append(item)
        print("\n".join(["".join(str(lemm_list[i:i + 10]))
                         for i in range(0, len(lemm_list), 10)]))
        print(f"LEMMATIZED TOKENS IN TOTAL: {len(lemm_list)}")
        return lemm_dict

    @staticmethod
    def stemming(text):
        """
        This method stems tokens of the text.

        :param text:(str)the text from the opened text file)

        Introduced variables:
        stem_list(list): the list of paired tokens - stemmed words
        tokens(list): tokenized words from the text
        token(str): one token(item) from the list of tokens
        port_stem(obj): initialized instance
                        of the 'PorterStemmer' class
        key, value(str): keys and values of the 'stem_dict' dictionary


        :return stem_dict(dict): pairs of token(key) - stemmed word(value)
        """
        stem_dict = {}
        stem_list = []
        tokens = nltk.word_tokenize(text)
        port_stem = nltk.stem.PorterStemmer()
        # (The dictionary has unique key names.
        #  Hence, the number of keys
        #  falls behind the number of tokenized words.)
        # (Словари имеют уникальные названия ключения,
        #  вследствии чего после создания словаря
        #  колличество ключей уступает колличеству
        #  токенизированных слов.)
        for token in tokens:
            stem_dict[token] = port_stem.stem(token)
        for key, value in stem_dict.items():
            item = key + ": " + value
            stem_list.append(item)
        print("\n".join(["".join(str(stem_list[i:i + 10]))
                         for i in range(0, len(stem_list), 10)]))
        print(f"STEMMED TOKENS IN TOTAL: {len(stem_list)}")
        return stem_dict

    @staticmethod
    def tagging(text):
        """
        This method tags tokens of the text.

        :param text:(str)the text from the opened text file)
        :return tags(list): a list of paired tuples of token - tag
        """
        tokens = nltk.word_tokenize(text)
        tags = nltk.pos_tag(tokens)
        print("\n".join(["".join(str(tags[i:i + 10]))
                         for i in range(0, len(tags), 10)]))
        print(f"TOKENS TAGGED IN TOTAL: {len(tags)}")

        return tags


class Systematization:
    """
    This class executes such natural language-processing operations
    as classification and lexical analysis.

    Methods:
    freq_output(): graphically outputs the results of work
                   of other methods of the class
    classifying(): executes frequency distribution of tokens
    analyzing(): executes lexical analysis of tokens
    """

    @staticmethod
    def freq_output(collection):
        """
        This method enumerates and outputs
        items of a collection.
        :param collection:(collection) any collection data type
        :return num(int): ordinal number of the last item
                          in the collection
        """
        num = 1
        for item in collection:
            print(f"{num}. {item}")
            num += 1
        return num

    @staticmethod
    def classifying(text):
        """
        This method executes frequency distribution of tokens.
        :param text:(str)the text from the opened text file)


        Introduced variables:
        stop_words(set): a set of English stop-words
        tokens(list): tokenized words from the text
        clear_text(list): tokenized words from the text
                          without stop-words
        freq, clear_freq(obj): initialized instances
                               of the 'PorterStemmer' class
        commons(list): a list of most frequent tokens in the text
        clear_commons, set_commons(list): lists of most frequent tokens
                                          in the text (without stop-words)
        set_freq(int): a custom number of most frequent tokens to display
        search(str): a custom word to check its frequency in the text

        :return freq(obj): initialized instances
                           of the 'PorterStemmer' class
        """
        stop_words = set(nltk.corpus.stopwords.words("english"))
        stop_words.update(",", ".", ":", ";", "?", "!")
        #
        tokens = nltk.word_tokenize(text.lower())
        freq = nltk.FreqDist(tokens)
        commons = freq.most_common()
        print("\nTOP USED TOKENS:")
        time.sleep(1)
        Systematization.freq_output(commons)
        time.sleep(1)
        #
        clear_tokens = [token for token in tokens if token not in stop_words]
        clear_freq = nltk.FreqDist(clear_tokens)
        clear_commons = clear_freq.most_common()
        print("\nTOP USED INFORMATIVE TOKENS (WITHOUT STOP-WORDS):")
        time.sleep(1)
        Systematization.freq_output(clear_commons)
        time.sleep(1)
        #
        print("\nPERSONAL LIST OF INFORMATIVE TOKENS (WITHOUT STOP-WORDS):")
        while True:
            try:
                set_freq = int(input("\nHow many most frequent "
                                     "cleared tokens do you want to view?: "))
                if set_freq <= 0:
                    print("Please, input only natural numbers.")
                    continue
                break
            except ValueError:
                print("Inadmissible characters or invalid input. "
                      "Please, only put natural numbers.")
        set_commons = clear_freq.most_common(set_freq)
        Systematization.freq_output(set_commons)
        time.sleep(1)
        #
        search = input("\nEnter your token to check its frequency in the text: ")
        print(f"The token '{search}' is used "
              f"{freq[search]} times through the text.")
        time.sleep(1)
        return freq

    @staticmethod
    def analyzing(text):
        """
        This method executes lexical analysis of tokens.

        Introduced variables:
        tokens(list): tokenized words from the text
        word(str): custom token to execute lexical analysis
        syn_set(set): unique synonyms for the custom token
        defs, ant_list(list): definitions and antonyms
                              for the selected token
        syn(synset item): a synonym from the synonym list
        lemma(lemma item): a lemma item in the synset object
        :param text:(str)the text from the opened text file)

        :return syns(list): synset items of synonyms for a token
        """
        tokens = nltk.word_tokenize(text.lower())
        print("\nTHE LIST OF AVAILABLE TOKENS:")
        print("\n".join(["".join(str(tokens[i:i + 25]))
                         for i in range(0, len(tokens), 25)]))
        while True:
            word = input("\nSelect a token to execute lexical analysis on: ")
            if word in tokens:
                syns = nltk.corpus.wordnet.synsets(word)
                defs = []
                syn_set = set()
                ant_list = []
                #
                for syn in syns:
                    defs.append(syn.definition())
                #
                for syn in syns:
                    for lemma in syn.lemmas():
                        # if lemma.name() != word and lemma.name() != lemma.name():
                        syn_set.add(lemma.name())
                        if lemma.antonyms():
                            ant_list.append(lemma.antonyms()[0].name())
                #
                print("\nKNOWN DEFINITIONS:")
                Systematization.freq_output(defs)
                if len(defs) < 1:
                    print("NO RELEVANT DEFINITIONS FOUND.")
                time.sleep(1)
                #
                print("\nRELEVANT SYNONYMS:")
                Systematization.freq_output(syn_set)
                if len(syn_set) < 1:
                    print("NO RELEVANT SYNONYMS FOUND.")
                time.sleep(1)
                #
                print("\nRELEVANT ANTONYMS:")
                Systematization.freq_output(ant_list)
                if len(ant_list) < 1:
                    print("NO RELEVANT ANTONYMS FOUND.")
                time.sleep(1)
                #
                break
            print("No such token in the text. Please, select again")
        return syns
