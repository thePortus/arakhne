"""
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

    def test_rm_lines(self):
        test = BaseCorpus([
            BaseDoc('Lorem\nipsum'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ]).rm_lines()
        compare = BaseDoc('Lorem ipsum')
        return self.assertEqual(test[0], compare)

    def test_rm_nonchars(self):
        test = BaseCorpus([
            BaseDoc('Lorem 3%ipsum'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ]).rm_nonchars()
        compare = BaseDoc('Lorem ipsum')
        return self.assertEqual(test[0], compare)

    def test_rm_edits(self):
        test = BaseCorpus([
            BaseDoc('Lorem[ ipsum]'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ]).rm_edits()
        compare = BaseDoc('Lorem')
        return self.assertEqual(test[0], compare)

    def test_rm_spaces(self):
        test = BaseCorpus([
            BaseDoc('Lorem  ipsum'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ]).rm_spaces()
        compare = BaseDoc('Lorem ipsum')
        return self.assertEqual(test[0], compare)

    def test_update(self):
        BaseCorpus([
            BaseDoc('Lorem  ipsum'),
            BaseDoc('Dolor sit'),
            BaseDoc('amet.')
        ]).update('Update message test', 1, 'ignore')
        return self.assertEqual(True, True)
"""
