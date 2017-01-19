import os
from collections import UserList

from ..settings import Defaults


class Stopwords(UserList):

    def __init__(self, path=None, language='english'):
        super().__init__()
        self.language = language
        if path:
            if os.path.isabs(path):
                self.path = path
            else:
                self.path = os.path.join(os.getcwd(), path)
            if self.check_file:
                self.load_file
            else:
                raise IOError('File does not exist at', self.path)
            self.load_file()
        else:
            self.load_default()

    def check_file(self):
        if os.path.exists(self):
            return True
        return False

    def load_file(self):
        # TODO: ADD SETTINGS COMPONENTS (E.G. Encoding)
        self.clear()
        with open(self.path, 'r+', encoding='utf-8') as stopfile:
            for stopword in stopfile.readlines():
                self.append(stopword.lower().strip())

    def load_default(self):
        self.path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            Defaults.STOPWORDS[self.language]
        )
        self.load_file()
