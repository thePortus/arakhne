"""Arakhne Corpus Constructor"""

from .setup import Validate, Install
from .corpus import Corpus


def Arakhne(language=None):
    # Ensure langauge is supported
    validator = Validate(language)
    installer = Install(language)
    if not validator.system():
        raise Exception(
            'Unsupported OS, Only POSIX and Windows Systems Supported'
        )
    needed_modules = validator.modules()
    needed_packages = validator.packages()
    if len(needed_modules) > 0:
        print('Python dependencies required, downloading...')
        print(needed_modules)
        installer.modules()
    # Ignores phi7 and tlg as they are not included by default
    if len(needed_packages) > 0 and needed_packages != ['phi7', 'tlg']:
        print('Linguistic packages required, downloading...')
        print(needed_packages)
        installer.packages()
    # Return an empty corpus of appropriate language
    return Corpus(language).make()
