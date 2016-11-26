import unittest

from .. import base


class CorpusUnitTest(unittest.TestCase):
    test_in = 'fixtures/prose_latin.csv'
    test_out = 'fixtures/test_files/test_out.csv'

    def test_csv_load(self):
        compare = base
        test = type(base().csv().load(self.test_in))
        return self.assertEqual(test, compare)

    def test_csv_save(self):
        compare = base().csv().load(self.test_in)
        test = compare.csv().save(self.test_out)
        return True
