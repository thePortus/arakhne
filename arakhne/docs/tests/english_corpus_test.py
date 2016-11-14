import unittest

from ..english_doc import EnglishDoc
from ..english_corpus import EnglishCorpus


class EnglishCorpusUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = EnglishCorpus([
            EnglishDoc('The quick'),
            EnglishDoc('brown fox'),
            EnglishDoc('jumped.')
        ])
        compare = 'The quick'
        return self.assertEqual(test[0], compare)

    def test_tokenize(self):
        EnglishCorpus([
            EnglishDoc('The quick'),
            EnglishDoc('brown fox'),
            EnglishDoc('jumped.')
        ]).tokenize()
        return True

    # TEMPORARILY DISABLED TO IMPROVE TEST RUN TIME
    """
    def test_lemmatize(self):
        EnglishCorpus([
            EnglishDoc('The quick'),
            EnglishDoc('brown fox'),
            EnglishDoc('jumped.')
        ]).lemmatize()
        return True
    """

    def test_rm_stopwords(self):
        EnglishCorpus([
            EnglishDoc('The quick'),
            EnglishDoc('brown fox'),
            EnglishDoc('jumped.')
        ]).rm_stopwords(['quick'])
        return True

    def test_ngrams(self):
        EnglishCorpus([
            EnglishDoc('The quick'),
            EnglishDoc('brown fox'),
            EnglishDoc('jumped.')
        ]).ngrams()
        return True

    def test_skipgrams(self):
        EnglishCorpus([
            EnglishDoc('The quick'),
            EnglishDoc('brown fox'),
            EnglishDoc('jumped.')
        ]).skipgrams()
        return True
