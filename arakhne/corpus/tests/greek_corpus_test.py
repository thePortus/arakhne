import unittest

from .. import greek
from ...get import Get


class GreekCorpusUnitTest(unittest.TestCase):
    test = greek().mk_doc(
        'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ'
    )

    @classmethod
    def setUpClass(cls):
        Get('greek').packages()
        return True

    @classmethod
    def tearDownClass(cls):
        return True

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
