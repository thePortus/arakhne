import nltk

from .get_base import GetBase


class GetNLTK(GetBase):
    pip_modules = ['nltk']

    def data(self, all=True):
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

    def test_data(self):
        test_packages = [
            'punkt',
            'maxent_treebank_pos_'
        ]
        for test_package in test_packages:
            try:
                nltk.download(test_package)
            except:
                raise OSError(
                    'Problem downloading NLTK Package:', test_package
                )
