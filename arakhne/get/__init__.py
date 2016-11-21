from .. import core
from .get_nltk import GetNLTK
from .get_cltk import GetCLTK


class Get:
    language = None
    getter = None

    def __init__(self, language):
        if core.languages.test_lang(language):
            self.language = language
            if self.language == 'latin' or self.language == 'greek':
                self.getter = GetCLTK()
            if self.language == 'english':
                self.getter = GetNLTK()

    def module(self):
        self.getter.install()
        return True

    def trainers(self):
        self.getter.data(language=self.language)
        return True

    def all(self):
        self.module()
        self.trainers()
        return True
