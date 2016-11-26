import unittest

from .. import Corpus, base, english, latin, greek


class CorpusUnitTest(unittest.TestCase):

    def test_base(self):
        compare = base
        test = type(Corpus().make([
            'The quick brown fox jumped over the lazy dog.'
        ]))
        return self.assertEqual(test, compare)

    def test_english(self):
        compare = english
        test = type(Corpus('english').make([
            'The quick brown fox jumped over the lazy dog.'
        ]))
        return self.assertEqual(test, compare)

    def test_latin(self):
        compare = latin
        test = type(Corpus('latin').make([
            'Id hoc facilius iis persuasit.'
        ]))
        return self.assertEqual(test, compare)

    def test_greek(self):
        compare = greek
        test = type(Corpus('greek').make([
            'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ.'
        ]))
        return self.assertEqual(test, compare)
