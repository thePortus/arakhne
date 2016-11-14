import unittest

from ..base_doc import BaseDoc
from ..base_corpus import BaseCorpus


class BaseCorpusUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = BaseCorpus([
            BaseDoc('Lorem ipsum'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ])
        compare = 'Lorem ipsum'
        return self.assertEqual(test[0], compare)

    def test_re_search_valid(self):
        test = BaseCorpus([
            BaseDoc('Lorem ipsum'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ]).re_search('amet')
        compare = BaseDoc('amet.')
        return self.assertEqual(test[0], compare)

    def test_re_search_invalid(self):
        test = BaseCorpus([
            BaseDoc('Lorem ipsum'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ]).re_search('amet')
        compare = BaseDoc('Arma virumque cano')
        return self.assertNotEqual(test[0], compare)
