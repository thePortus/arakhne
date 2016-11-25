import unittest

from .. import Doc


class GreekDocUnitTest(unittest.TestCase):
    test = Doc('greek').make(
        'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ'
    )

    def test_normalize(self):
        compare = 'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ'
        test = self.test.normalize()
        return self.assertEqual(test, compare)

    def test_tlgu_cleanup(self):
        compare = 'ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ'
        test = self.test.tlgu_cleanup()
        return self.assertEqual(test, compare)

    def test_tag_123(self):
        compare = ('ὁ', 'P-S---MN-')
        test = self.test.tag(mode='123')[0]
        return self.assertEqual(test, compare)

    def test_tag_tnt(self):
        compare = ('ὁ', 'P-S---MN-')
        test = self.test.tag(mode='tnt')[0]
        return self.assertEqual(test, compare)
