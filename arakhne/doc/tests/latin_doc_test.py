import unittest

from .. import Doc
from ...get import Get


class LatinDocUnitTest(unittest.TestCase):
    test = Doc('latin').make(
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
        test = self.test.normalize()
        return self.assertEqual(test, compare)

    def test_stemmify(self):
        compare = 'cu re verisimil caus adfereba '
        test = self.test.stemmify()
        return self.assertEqual(test, compare)

    # ADD TEST MACRONIZE
