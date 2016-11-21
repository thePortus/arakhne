"""
import unittest

from .. import Get, GetNLTK


class GetUnitTest(unittest.TestCase):

    def test_invalid_init(self):
        with self.assertRaises(TypeError):
            Get('not_a_language')

    def test_valid_init(self):
        test = type(Get('english').getter)
        compare = GetNLTK
        return self.assertEqual(test, compare)

    def test_module(self):
        test = Get('english').module()
        compare = True
        return self.assertEqual(test, compare)
"""
