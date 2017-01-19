import nltk

from .get_base import GetBase
from ..core import settings


class GetNLTK(GetBase):
    pip_modules = ['nltk']

    def packages(self):
        test_packages = settings.NLTK_PACKAGES
        for test_package in test_packages:
            try:
                nltk.download(test_package)
            except:
                raise OSError(
                    'Problem downloading NLTK Package:', test_package
                )
