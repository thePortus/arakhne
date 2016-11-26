import unittest

from .. import Arakhne


class ArakhneUnitTest(unittest.TestCase):

    def test_functionality(self):
        compare = Arakhne
        test = Arakhne()
        test = type(test)
        return self.assertEqual(test, compare)
