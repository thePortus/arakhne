import unittest

from ..validate import Validate


class TestInvalidLanguage(unittest.TestCase):
    language = 'pseudolingua'

    def test_exception_raised(self):
        with self.assertRaises(Exception):
            Validate(self.language)


class TestBaseValidate(unittest.TestCase):
    language = None
    validator = None

    def setup(self):
        self.validator = Validate(self.language)

    def test_system(self):
        self.setup()
        test = self.validator.system()
        compare = True
        return self.assertEqual(test, compare)

    def test_modules(self):
        self.setup()
        test = type(self.validator.modules())
        compare = list
        return self.assertEqual(test, compare)

    def test_packages(self):
        self.setup()
        test = type(self.validator.packages())
        compare = list
        return self.assertEqual(test, compare)


class TestNLTKValidate(TestBaseValidate):
    language = 'english'


class TestCLTKValidate(TestBaseValidate):
    language = 'latin'
