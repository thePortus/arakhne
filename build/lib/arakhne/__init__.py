from . import core
from .corpus import Corpus


class Arakhne:
    language = None
    corpus = None

    def corpus(self, language=None):
        # Ensure language is a string
        if core.languages.test_lang(language):
            # If default language not set, store language at .language
            if not self.language:
                self.language = language
        return Corpus(language).make(docs=[])
