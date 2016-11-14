import unittest

from .. import Arakhne
from ..docs.latin_corpus import LatinCorpus


class ArakhneUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = Arakhne(language='latin').corpus.load.csv(
            path='tests/fixtures/prose_latin.csv',
        )
        compare = LatinCorpus
        return self.assertEqual(type(test), compare)
