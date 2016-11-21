from . import settings
from collections import UserList


class LanguageChecker(UserList):

    def __init__(self):
        super().__init__()
        for language in settings.SUPPORTED_LANGS:
            self.data.append(language)

    def check_lang(self, language):
        valid = False
        for supported_language in self.data.name:
            if language == supported_language:
                valid = True
        return valid

    def test_lang(self, language):
        if not self.check_lang(language):
            raise TypeError(
                'Invalid language, supported languages:',
                self.data
            )
            return False
        return True

    def get_doc(self, language):
        self.test_lang(language)
        return settings.LANG_OBJECTS[language]['doc']

    def get_corpus(self, language):
        self.test_lang(language)
        return settings.LANG_OBJECTS[language]['corpus']
