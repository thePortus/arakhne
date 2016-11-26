"""
import unittest

from .. import Get, GetCLTK


class GetCLTKUnitTest(unittest.TestCase):

    def test_get_corpora(self):
        test = Get('latin').trainers()
        compare = True
        return self.assertEqual(test, compare)
"""
