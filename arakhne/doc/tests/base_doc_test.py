import unittest

from .. import Doc


class BaseDocUnitTest(unittest.TestCase):
    test = Doc().make(
        '123 The quick [quack] brown  \nfox jumped over the lazy dog.'
    )

    def test_rm_lines(self):
        compare = '123 The quick [quack] brown   fox jumped over the lazy dog.'
        test = self.test.rm_lines()
        return self.assertEqual(test, compare)

    def test_rm_nonchars(self):
        compare = ' The quick quack brown  fox jumped over the lazy dog'
        test = self.test.rm_nonchars()
        return self.assertEqual(test, compare)

    def test_rm_edits(self):
        compare = '123 The quick  brown  \nfox jumped over the lazy dog.'
        test = self.test.rm_edits()
        return self.assertEqual(test, compare)

    def test_rm_spaces(self):
        compare = '123 The quick [quack] brown fox jumped over the lazy dog.'
        test = self.test.rm_spaces()
        return self.assertEqual(test, compare)

    def test_rm_stopwords(self):
        compare = '123 The [quack] brown fox jumped over the lazy dog.'
        test = self.test.rm_stopwords(['quick'])
        return self.assertEqual(test, compare)

    def test_re_search(self):
        compare = True
        test = self.test.re_search('brown')
        return self.assertEqual(test, compare)

    def test_stringify(self):
        compare = str
        test = type(self.test.stringify())
        return self.assertEqual(test, compare)
