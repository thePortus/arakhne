import unittest

from ..latin_doc import LatinDoc
from ..latin_corpus import LatinCorpus


class LatinCorpusUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = LatinCorpus([
            LatinDoc('Cuius rei'),
            LatinDoc('verisimilis causa'),
            LatinDoc('adferebatur, quod Gallis')
        ])
        compare = 'Cuius rei'
        return self.assertEqual(test[0], compare)
