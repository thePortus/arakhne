from .test_base_doc import AbstractTestDoc


class TestNLTKDoc(AbstractTestDoc):
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'
    language = 'english'

    def test_tokenize_word(self):
        self.setup()
        test = len(self.doc.tokenize())
        compare = 14
        return self.assertEqual(test, compare)

    def test_tokenize_sentence(self):
        self.setup()
        test = len(self.doc.tokenize(mode='sentence'))
        compare = 1
        return self.assertEqual(test, compare)

    def test_tokenize_wordpunct(self):
        self.setup()
        test = len(self.doc.tokenize(mode='wordpunct'))
        compare = 15
        return self.assertEqual(test, compare)

    def test_tag(self):
        self.setup()
        test = type(self.doc.tag()[0])
        compare = tuple
        return self.assertEqual(test, compare)

    def test_lemmatize(self):
        self.setup()
        test = len(self.doc.lemmatize())
        compare = 54
        return self.assertEqual(test, compare)

    def test_rm_stopwords(self):
        self.setup()
        test = self.doc.rm_stopwords(['fox'])
        compare = 'The quick bro- wn jumped ov3r [ sic ] the lazy dog.'
        return self.assertEqual(test, compare)

    def test_ngrams(self):
        self.setup()
        test = len(self.doc.ngrams())
        compare = 12
        return self.assertEqual(test, compare)

    def test_skipgrams(self):
        self.setup()
        test = len(self.doc.skipgrams())
        compare = 34
        return self.assertEqual(test, compare)
