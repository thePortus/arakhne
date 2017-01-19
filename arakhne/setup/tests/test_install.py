import unittest

from ..install import Install


class TestInvalidLanguage(unittest.TestCase):
    language = 'pseudolingua'

    def test_exception_raised(self):
        with self.assertRaises(Exception):
            Install(self.language)


class TestBaseValidate(unittest.TestCase):
    language = None
    install = None

    def setup(self):
        self.install = Install(self.language)

    def test_modules(self):
        self.setup()
        test = self.install.modules()
        compare = True
        return self.assertEqual(test, compare)

    def test_packages(self):
        self.setup()
        test = self.install.packages()
        compare = True
        return self.assertEqual(test, compare)

    def test_all(self):
        self.setup()
        test = self.install.all()
        compare = True
        return self.assertEqual(test, compare)


class TestNLTKValidate(TestBaseValidate):
    language = 'english'


class TestCLTKValidate(TestBaseValidate):
    language = 'latin'
