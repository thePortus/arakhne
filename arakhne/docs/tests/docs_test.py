import unittest

from .. import Docs
from ..latin_corpus import LatinCorpus


class DocsUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = Docs(language='latin').corpus.load.csv(
            'tests/fixtures/prose_latin.csv'
        )
        compare = LatinCorpus
        return self.assertEqual(type(test), compare)
