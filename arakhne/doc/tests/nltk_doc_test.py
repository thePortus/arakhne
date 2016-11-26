import unittest

from .. import Doc
from ...get import Get


class NLTKDocUnitTest(unittest.TestCase):
    test = Doc('english').make(
        'The quick brown fox jumped over the lazy dog.'
    )

    def setupAll(self):
        Get('english').test_data()

    def teardownAll(self):
        pass

    def test_tag(self):
        compare = ('The', 'DT')
        test = self.test.tag()[0]
        return self.assertEqual(test, compare)

    def test_tokenize(self):
        compare = [
            'The', 'quick', 'brown', 'fox', 'jumped',
            'over', 'the', 'lazy', 'dog', '.'
        ]
        test = self.test.tokenize()
        return self.assertEqual(test, compare)

    """
    def test_lemmatize(self):
        compare = 'The quick brown fox jump over the lazy dog .'
        test = self.test.lemmatize()
        return self.assertEqual(test, compare)

    def test_rm_stopwords(self):
        compare = 'The quick brown fox over the lazy dog.'
        test = self.test.rm_stopwords(['jumped'])
        return self.assertEqual(test, compare)

    def test_ngrams(self):
        compare = ('The', 'quick', 'brown')
        test = self.test.ngrams()[0]
        return self.assertEqual(test, compare)

    def test_skipgrams(self):
        compare = ('The', 'quick', 'brown')
        test = self.test.skipgrams()[0]
        return self.assertEqual(test, compare)
    """
