from .. import languages

import unittest


class LanguageCheckerUnitTest(unittest.TestCase):

    def test_invalid_language_check(self):
        return self.assertEquals(languages.check_lang('not_a_language'), False)

    def test_invalid_language_test(self):
        with self.assertRaises(TypeError):
            languages.test_lang('not_a_language')
