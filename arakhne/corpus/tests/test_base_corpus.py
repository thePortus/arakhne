import unittest

from .. import Corpus


class AbstractTestCorpus(unittest.TestCase):
    text = None
    language = None
    corpus = None

    def setup(self):
        self.corpus = Corpus(self.language).make().mk_doc(self.text)


class TestBaseCorpus(AbstractTestCorpus):
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'

    def test_rm_lines(self):
        self.setup()
        test = self.corpus.rm_lines()
        compare = ['The quick brown fox   jumped ov3r[sic] the lazy dog.']
        return self.assertEqual(test, compare)

    def test_rm_nonchars(self):
        self.setup()
        test = self.corpus.rm_nonchars()
        compare = ['Thequick brown fox   jumped ovrsic the lazy dog']
        return self.assertEqual(test, compare)

    def test_rm_edits(self):
        self.setup()
        test = self.corpus.rm_edits()
        compare = ['The\nquick bro-\nwn fox   jumped ov3r the lazy dog.']
        return self.assertEqual(test, compare)

    def test_rm_spaces(self):
        self.setup()
        test = self.corpus.rm_spaces()
        compare = ['The quick bro- wn fox jumped ov3r[sic] the lazy dog.']
        return self.assertEqual(test, compare)

    def test_rm_stopwords(self):
        self.setup()
        test = self.corpus.rm_stopwords(['fox'])
        compare = ['The quick bro- wn jumped ov3r[sic] the lazy dog.']
        return self.assertEqual(test, compare)

    def test_re_search(self):
        self.setup()
        test = self.corpus.re_search('fox')
        compare = ['The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.']
        return self.assertEqual(test, compare)

    def test_re_search_not_present(self):
        self.setup()
        test = self.corpus.re_search('bulbous bouffant')
        compare = []
        return self.assertEqual(test, compare)
