from .test_base_corpus import AbstractTestCorpus
from ...tests import LatinFixtureLayer

class TestLatinCorpus(AbstractTestCorpus):
    text = 'Omnia gallia\nin tres part-\nes divisa est.'
    language = 'latin'
    layer = LatinFixtureLayer

    def test_normalize(self):
        self.ready()
        test = len(self.corpus.normalize())
        compare = 1
        return self.assertEqual(test, compare)

    def test_stemmify(self):
        self.ready()
        test = len(self.corpus.stemmify())
        compare = 1
        return self.assertEqual(test, compare)
