"""
import unittest

from .. import greek


class GreekCorpusUnitTest(unittest.TestCase):
    test = greek().mk_doc(
        'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ'
    )

    def test_normalize(self):
        compare = 'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ'
        test = self.test.normalize()[0]
        return self.assertEqual(test, compare)

    def test_tlgu_cleanup(self):
        compare = 'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ'
        test = self.test.tlgu_cleanup()[0]
        return self.assertEqual(test, compare)

    def test_tag(self):
        compare = ('ὁ', 'P-S---MN-')
        test = self.test.tag()[0][0]
        return self.assertEqual(test, compare)
"""
