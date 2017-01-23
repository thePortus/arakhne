import unittest

from ... import Arakhne
from .. import Doc
from ...tests import BaseFixtureLayer


class AbstractTestDoc(unittest.TestCase):
    text = None
    language = None
    doc = None
    layer = BaseFixtureLayer

    def ready(self):
        self.doc = Doc(self.language).make(self.text)


class TestBaseDoc(AbstractTestDoc):
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'

    def test_rm_lines(self):
        self.ready()
        test = self.doc.rm_lines()
        compare = 'The quick brown fox   jumped ov3r[sic] the lazy dog.'
        return self.assertEqual(test, compare)

    def test_rm_nonchars(self):
        self.ready()
        test = self.doc.rm_nonchars()
        compare = 'Thequick brown fox   jumped ovrsic the lazy dog'
        return self.assertEqual(test, compare)

    def test_rm_edits(self):
        self.ready()
        test = self.doc.rm_edits()
        compare = 'The\nquick bro-\nwn fox   jumped ov3r the lazy dog.'
        return self.assertEqual(test, compare)

    def test_rm_spaces(self):
        self.ready()
        test = self.doc.rm_spaces()
        compare = 'The quick bro- wn fox jumped ov3r[sic] the lazy dog.'
        return self.assertEqual(test, compare)

    def test_rm_stopwords(self):
        self.ready()
        test = self.doc.rm_stopwords(['fox'])
        compare = 'The quick bro- wn jumped ov3r[sic] the lazy dog.'
        return self.assertEqual(test, compare)

    def test_re_search(self):
        self.ready()
        test = self.doc.re_search('fox')
        compare = True
        return self.assertEqual(test, compare)

    def test_re_search_not_present(self):
        self.ready()
        test = self.doc.re_search('bulbous bouffant')
        compare = False
        return self.assertEqual(test, compare)

    def test_stringify(self):
        self.ready()
        test = type(self.doc.stringify())
        compare = str
        return self.assertEqual(test, compare)
