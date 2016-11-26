import nltk

from .get_base import GetBase


class GetNLTK(GetBase):
    pip_modules = ['nltk']

    def data(self, language='english', all=True):
        print('Launching NLTK Downloader')
        print('Depending on your system, this may take a moment.')
        try:
            if all:
                nltk.download('all')
            else:
                nltk.download()
        except:
            raise OSError('Problem downloading NLTK packages')
        return True
