import unittest

from ..greek_doc import GreekDoc


class GreekDocUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = GreekDoc('ὁ δὲ δῆμος.')
        compare = 'ὁ δὲ δῆμος.'
        return self.assertEqual(test, compare)

    def test_tokenize(self):
        test = GreekDoc('ὁ δὲ δῆμος.').tokenize()
        compare = ['ὁ', 'δὲ', 'δῆμος', '.']
        return self.assertEqual(test, compare)

    def test_tlgu_cleanup(self):
        test = GreekDoc('ERRORὁ δὲ δῆμος.').tlgu_cleanup()
        compare = 'ὁ δὲ δῆμος.'
        return self.assertEqual(test, compare)

    def test_entities(self):
        test = GreekDoc('ὁ δὲ Πειραιεὺς δῆμος.').entities()
        compare = ['Πειραιεὺς']
        return self.assertEqual(test, compare)

    def test_word_count(self):
        GreekDoc('ὁ δὲ δῆμος.').word_count()
        return True

    def test_compare_levenstein(self):
        GreekDoc('ὁ δὲ δῆμος.').compare_levenshtein('ὁ δὲ Πειραιεὺς δῆμος.')
        return True

    def test_normalize(self):
        GreekDoc('ὁ δὲ δῆμος.').normalize()
        return True

    def test_tag(self):
        GreekDoc('ὁ δὲ δῆμος.').tag()
        return True
