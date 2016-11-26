import unittest

from .. import latin
from ...get import Get


class LatinCorpusUnitTest(unittest.TestCase):
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

    def test_normalize(self):
        compare = 'Cuius rei uerisimilis causa adferebatur'
        test = self.test.normalize()[0]
        return self.assertEqual(test, compare)

    def test_stemmify(self):
        compare = 'cu re verisimil caus adfereba '
        test = self.test.stemmify()[0]
        return self.assertEqual(test, compare)

    # RE-ADD TEST MACRONIZE
    # def test_macronize(self):
    #     compare = 'cu re verisimil caus adfereba '
    #     test = self.test.macronize()[0]
    #     return self.assertEqual(test, compare)

    def test_clausulae(self):
        compare = 0
        test = latin().mk_doc([
            'rancidum aprum antiqui laudabant, non quia nasus',
            'illis nullus erat, sed, credo, hac mente, quod hospes',
            'tardius adveniens vitiatum commodius quam',
        ])
        test = test.clausulae()[0]['cretic + iamb']
        return self.assertEqual(test, compare)
