"""Setup module for Arakhne"""

from .validate import Validate
from .install import Install

__author__ = 'David J. Thomas <dave.a.base@gmail.com>'
__license__ = 'MIT License. See LICENSE.'


class Setup:

    def __init__(self, language=None):
        self.language = language
        self.validator = Validate(language)
        self.installer = Install(language)
        # Ensure OS compatibility before proceeding
        if not self.validator.system():
            raise Exception(
                'Unsupported OS, Only POSIX and Windows Systems Supported'
            )

    def modules(self):
        # Checks for and installs Python dependencies via pip
        needed = self.validator.modules()
        if type(needed) == list:
            if len(needed) > 0:
                print('Python dependencies required, downloading', needed)
                self.installer.modules(needed)
                print('Python dependencies installed successfully')
        return True

    def packages(self):
        # Checks for and installs necessary NLTK and CLTK linguistic data
        needed = self.validator.packages()
        # Ignores phi7 and tlg as they are not included by default
        if type(needed) == list:
            if len(needed) > 0:
                print('NLTK & CLTK linguistic data required, downloading', needed)
                self.installer.packages(needed)
                print('NLTK & CLTK linguistic data installed successfully')
        return True

    def setup(self):
        # Checks for and installs all additional software/data
        if self.modules() and self.packages():
            return True
        return False
