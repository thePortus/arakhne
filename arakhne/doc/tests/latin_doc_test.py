"""
import unittest

from .. import Doc


class LatinDocUnitTest(unittest.TestCase):
    test = Doc('latin').make(
        'Cuius rei verisimilis causa adferebatur'
    )

    def test_normalize(self):
        compare = 'Cuius rei uerisimilis causa adferebatur'
        test = self.test.normalize()
        return self.assertEqual(test, compare)

    def test_stemmify(self):
        compare = 'cu re verisimil caus adfereba '
        test = self.test.stemmify()
        return self.assertEqual(test, compare)

    # ADD TEST MACRONIZE
"""
