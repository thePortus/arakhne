import unittest

from .. import Doc, base, english, latin, greek


class DocUnitTest(unittest.TestCase):

    def test_base(self):
        compare = base
        test = type(Doc().make(
            'The quick brown fox jumped over the lazy dog.'
        ))
        return self.assertEqual(test, compare)

    def test_english(self):
        compare = english
        test = type(Doc('english').make(
            'The quick brown fox jumped over the lazy dog.'
        ))
        return self.assertEqual(test, compare)

    def test_latin(self):
        compare = latin
        test = type(Doc('latin').make(
            'Id hoc facilius iis persuasit.'
        ))
        return self.assertEqual(test, compare)

    def test_greek(self):
        compare = greek
        test = type(Doc('greek').make(
            'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ.'
        ))
        return self.assertEqual(test, compare)
