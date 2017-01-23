# import nltk - IMPORTED INLINE
# import cltk - IMPORTED INLINE

import pip

from ..settings import setup
from .validate import Validate


def Install(language):
    # Returns a Install specific to NLTK or CLTK
    if language in setup.NLTK_LANGS:
        return NLTKInstall(language)
    elif language in setup.CLTK_LANGS:
        return CLTKInstall(language)
    # Otherwise return the base Install
    elif not language:
        return BaseInstall(language)
    else:
        raise Exception(
            language +
            ' is unsupported. Supported languages are ' +
            setup.NLTK_LANGS
        )


class BaseInstall:
    language = None
    validator = None

    def __init__(self, language):
        self.language = language
        self.validator = Validate(self.language)

    def modules(self, needed):
        needed = self.validator.modules()
        if type(needed) == list:     # pragma: no cover
            if len(needed) > 0:
                print('Python modules required to continue, downloading...')
                for module in needed:
                    pip.main(['install', module])
        return True

    def packages(self):
        return True

    def all(self):
        return self.modules() and self.packages()


class NLTKInstall(BaseInstall):

    def packages(self, needed):
        # Inline import to prevent Exception for non NLTK users
        import nltk
        if type(needed) == list:
            if len(needed) > 0:
                print('NLTK trainer data required to continue, downloading...')
                for package in needed:
                    nltk.download(package)
        return True


class CLTKInstall(BaseInstall):

    def packages(self, needed):
        # Inline import to prevent Exception for non CLTK users
        from cltk.corpus.utils.importer import CorpusImporter
        if type(needed) == list:
            if len(needed) > 0:
                print('CLTK trainer data required to continue, downloading...')
                for package in needed:
                    try:
                        CorpusImporter(self.language).import_corpus(package)
                    except AttributeError:
                        # Bypass exceptions caused by obsolete corpora
                        pass
        return True
