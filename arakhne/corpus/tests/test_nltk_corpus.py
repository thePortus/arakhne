from .test_base_corpus import AbstractTestCorpus


class TestNLTKCorpus(AbstractTestCorpus):
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'
    language = 'english'

    def test_tokenize_word(self):
        self.setup()
        test = len(self.corpus.tokenize())
        compare = 1
        return self.assertEqual(test, compare)

    def test_lemmatize(self):
        self.setup()
        test = len(self.corpus.lemmatize())
        compare = 1
        return self.assertEqual(test, compare)

    def test_ngrams(self):
        self.setup()
        test = len(self.corpus.ngrams())
        compare = 1
        return self.assertEqual(test, compare)

    def test_skipgrams(self):
        self.setup()
        test = len(self.corpus.skipgrams())
        compare = 1
        return self.assertEqual(test, compare)
