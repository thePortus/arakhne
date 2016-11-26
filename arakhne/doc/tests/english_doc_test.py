import unittest

from .. import Doc


class EnglishDocUnitTest(unittest.TestCase):
    test = Doc('english').make(
        'The quick brown fox jumped over the lazy dog.'
    )

    def test_functionality(self):
        pass
