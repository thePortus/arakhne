from nltk.tokenize.punkt import PunktLanguageVars
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.util import ngrams, bigrams, trigrams, skipgrams
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

from .base_doc import BaseDoc


class NLTKDoc(BaseDoc):

    def tokenize(self, mode='word'):
        if mode == 'sentence':
            return (
                sent_tokenize(self.data)
            )
        elif mode == 'wordpunct':
            return wordpunct_tokenize(self.data)
        else:
            return word_tokenize(self.data)

    def tag(self):
        word_list = list(self.tokenize())
        return pos_tag(word_list)

    def lemmatize(self):
        tagged_words = self.tag()
        lemmata = []
        lemmatizer = WordNetLemmatizer()
        for word, parsing in tagged_words:
            # Grab main part of speech from first character in POS
            pos = parsing[0]
            try:
                lemmatized_word = lemmatizer.lemmatize(
                    word.lower(), pos=pos.lower()[0]
                )
            except:
                lemmatized_word = word
            lemmata.append(lemmatized_word)
        return self.__class__(
            " ".join(lemmata),
            self.metadata
        )

    def rm_stopwords(self, stoplist=[]):
        filtered_words = []
        # converts text to list of words with NLTK tokenizer
        tokenizer = PunktLanguageVars()
        tokens = tokenizer.word_tokenize(str(self.data))
        # loop through each word, if not in stoplist, append
        for word in tokens:
            not_found = True
            for stopword in stoplist:
                if str(word).strip().lower() == str(stopword).strip().lower():
                    not_found = False
            if not_found:
                filtered_words.append(word)
        # return rejoined word
        return self.__class__(
            " ".join(filtered_words),
            self.metadata
        )

    def ngrams(self, gram_size=3):
        tokens = self.tokenize()
        if gram_size < 2:   # pragma: no cover
            gram_size = 2
        if gram_size == 2:  # pragma: no cover
            return list(bigrams(tokens))
        if gram_size == 3:
            return list(trigrams(tokens))
        else:   # pragma: no cover
            return list(ngrams(tokens, gram_size))

    def skipgrams(self, gram_size=3, skip_size=1):
        tokens = self.tokenize()
        return list(skipgrams(tokens, gram_size, skip_size))
