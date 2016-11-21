"""
import unittest

from .. import Doc, BaseDoc, EnglishDoc, LatinDoc, GreekDoc


class DocUnitTest(unittest.TestCase):

    def test_base(self):
        compare = BaseDoc
        test = type(Doc(
            'The quick brown fox jumped over the lazy dog.'
        ))
        return self.assertEqual(test, compare)
"""
