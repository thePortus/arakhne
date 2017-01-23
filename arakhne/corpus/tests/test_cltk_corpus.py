from .test_base_corpus import AbstractTestCorpus
from ...tests import LatinFixtureLayer

class TestCLTKCorpus(AbstractTestCorpus):
    text = 'Omnia gallia\nin tres part-\nes divisa est.'
    language = 'latin'
    layer = LatinFixtureLayer

    def test_entities(self):
        self.ready()
        test = len(self.corpus.entities())
        compare = 1
        return self.assertEqual(test, compare)

    """
    def test_lemmatize(self):
        self.ready()
        test = len(self.corpus.lemmatize())
        compare = 1
        return self.assertEqual(test, compare)

    def test_scansion(self):
        self.ready()
        test = len(self.corpus.scansion())
        compare = 1
        return self.assertEqual(test, compare)
    """
