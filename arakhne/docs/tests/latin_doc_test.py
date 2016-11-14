import unittest

from ..latin_doc import LatinDoc


class LatinDocUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = LatinDoc('Lorem ipsum.')
        compare = 'Lorem ipsum.'
        return self.assertEqual(test, compare)
