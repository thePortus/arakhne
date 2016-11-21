import nltk

from .get_base import GetBase


class GetNLTK(GetBase):
    pip_modules = ['nltk']

    def data(self, language='english'):
        print('Launching NLTK Downloader')
        print('Depending on your system, this may take a moment.')
        try:
            nltk.download()
        except:
            return True
        return True
