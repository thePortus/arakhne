from . import core


class Arakhne:
    language = None

    def __init__(self, language=None):
        # Ensure language is a string
        if core.languages.test_lang(language):
            # Store language at .language
            self.language = language
