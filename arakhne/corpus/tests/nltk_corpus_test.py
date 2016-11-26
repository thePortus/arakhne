import unittest

from .. import english
from ...get import Get


class NLTKCorpusUnitTest(unittest.TestCase):
    test = english().mk_doc(
        '123 The quick [quack] brown  \nfox jumped over the lazy dog.'
    )

    @classmethod
    def setUpClass(cls):
        Get('english').test_data()
        return True

    @classmethod
    def tearDownClass(cls):
        return True

    def test_tokenize(self):
        compare = [
            '123', 'The', 'quick', '[', 'quack', ']', 'brown',
            'fox', 'jumped', 'over', 'the', 'lazy', 'dog', '.'
        ]
        test = self.test.tokenize()[0]
        return self.assertEqual(test, compare)

    def test_lemmatize(self):
        compare = '123 The quick [ quack ] brown fox jump over the lazy dog .'
        test = self.test.lemmatize()[0]
        return self.assertEqual(test, compare)

    def test_ngrams(self):
        compare = ('123', 'The', 'quick')
        test = self.test.ngrams()[0][0]
        return self.assertEqual(test, compare)

    def test_skipgrams(self):
        compare = ('123', 'The', 'quick')
        test = self.test.skipgrams()[0][0]
        return self.assertEqual(test, compare)
