import unittest

from .. import Stopwords


class TestStopwords(unittest.TestCase):

    def test_default(self):
        test = Stopwords()
        compare = Stopwords('arakhne/stopwords/defaults/english.txt')
        return self.assertEqual(test, compare)
