from .test_base_corpus import AbstractTestCorpus
from ...tests import GreekFixtureLayer

class TestGreekCorpus(AbstractTestCorpus):
    text = 'Ἡροδότου Ἁλικαρνησσέος ἱστορίης ἀπόδεξις ἥδε'
    language = 'greek'
    layer = GreekFixtureLayer

    def test_normalize(self):
        self.ready()
        test = len(self.corpus.normalize())
        compare = 1
        return self.assertEqual(test, compare)

    def test_tlgu_cleanup(self):
        self.ready()
        test = len(self.corpus.tlgu_cleanup())
        compare = 1
        return self.assertEqual(test, compare)

    def test_tag(self):
        self.ready()
        test = len(self.corpus.tag())
        compare = 1
        return self.assertEqual(test, compare)
