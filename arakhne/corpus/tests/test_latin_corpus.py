from .test_base_corpus import AbstractTestCorpus


class TestLatinCorpus(AbstractTestCorpus):
    text = 'Omnia gallia\nin tres part-\nes divisa est.'
    language = 'latin'

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
