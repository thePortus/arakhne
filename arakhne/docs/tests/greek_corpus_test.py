import unittest

from ..greek_doc import GreekDoc
from ..greek_corpus import GreekCorpus


class GreekCorpusUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = GreekCorpus([
            GreekDoc('ὁ δὲ Πειραιεὺς'),
            GreekDoc('δῆμος μὲν ἦν ἐκ παλαιοῦ,'),
            GreekDoc('πρότερον δὲ')
        ])
        compare = 'ὁ δὲ Πειραιεὺς'
        return self.assertEqual(test[0], compare)
