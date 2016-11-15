import unittest

from ..latin_doc import LatinDoc


class LatinDocUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = LatinDoc('Lorem ipsum.')
        compare = 'Lorem ipsum.'
        return self.assertEqual(test, compare)

    def test_normalize(self):
        LatinDoc('Lorem ipsum').normalize()
        return True

    def test_stemmify(self):
        LatinDoc('Lorem ipsum').stemmify()
        return True
