import unittest

from .. import latin


class CLTKCorpusUnitTest(unittest.TestCase):
    test = latin().mk_doc(
        'Cuius rei verisimilis causa adferebatur'
    )

    def test_entities(self):
        compare = ['Cuius']
        test = self.test.entities()[0]
        return self.assertEqual(test, compare)

    # ADD TEST LEMMATIZE
    # ADD TEST SCANSION
