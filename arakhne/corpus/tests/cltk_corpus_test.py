import unittest

from .. import latin
from ...get import Get


class CLTKCorpusUnitTest(unittest.TestCase):
    test = latin().mk_doc(
        'Cuius rei verisimilis causa adferebatur'
    )

    @classmethod
    def setUpClass(cls):
        Get('latin').packages()
        return True

    @classmethod
    def tearDownClass(cls):
        return True

    def test_entities(self):
        compare = ['Cuius']
        test = self.test.entities()[0]
        return self.assertEqual(test, compare)

    # ADD TEST LEMMATIZE
    # ADD TEST SCANSION
