import unittest

from ..base_doc import BaseDoc


class BaseDocUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = BaseDoc('Lorem ipsum.')
        compare = 'Lorem ipsum.'
        return self.assertEqual(test, compare)

    def test_re_search_valid(self):
        test = BaseDoc('Lorem ipsum')
        compare = ('ipsum')
        return self.assertTrue(test.re_search(compare))

    def test_re_search_invalid(self):
        test = BaseDoc('Lorem ipsum')
        compare = ('dolor')
        return self.assertFalse(test.re_search(compare))
