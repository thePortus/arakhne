import os
import importlib

from ..settings import setup


def Validate(language):
    # Returns a Validator specific to NLTK or CLTK
    if language in setup.NLTK_LANGS:
        return NLTKValidator(language)
    elif language in setup.CLTK_LANGS:
        return CLTKValidator(language)
    elif not language:
        return BaseValidator(language)
    else:
        raise Exception(
            language +
            ' is unsupported. Supported languages are ' +
            setup.NLTK_LANGS
        )


class BaseValidator:
    _systems = setup.SUPPORTED_SYSTEMS['base']
    _modules = []
    _packages = []

    def __init__(self, language):
        self.language = language

    def system(self):
        # Returns True if the current os is valid, False if not
        if os.name in self._systems:
            return True
        return False

    def modules(self):
        # Returns True if all Python modules are downloaded
        # Returns a list of missing modules otherwise
        needed = []
        for module in self._modules:
            try:
                importlib.find_loader(module)
            except:
                needed.append(module)
        # Return needed packages
        if len(needed) > 0:
            return needed
        else:
            return False

    def packages(self):
        # Returns False as the base Validator needs no packages
        return False


class NLTKValidator(BaseValidator):
    _systems = setup.SUPPORTED_SYSTEMS['nltk']
    _modules = setup.MODULES['nltk']
    _packages = setup.PACKAGES['nltk']

    def packages(self):
        needed = []
        import nltk
        req_data = self._packages['all'] + self._packages[self.language]
        for required in req_data:
            try:
                nltk.data.find(required[1])
            except:
                needed.append(required[0])
        # Return needed packages
        if len(needed) > 0:
            return needed
        else:
            return False


class CLTKValidator(BaseValidator):
    _systems = setup.SUPPORTED_SYSTEMS['cltk']
    _modules = setup.MODULES['cltk']
    _packages = setup.PACKAGES['cltk']

    def packages(self):
        from cltk.corpus.utils.importer import CLTK_DATA_DIR
        needed = []
        root_location = os.path.expanduser(CLTK_DATA_DIR + '/' + self.language)
        module_name = 'cltk.corpus.' + self.language + '.corpora'
        # Dynamically loading corpus attribute from module
        corpus_module = importlib.import_module(module_name)
        corpora = getattr(corpus_module, self.language.upper() + '_CORPORA')
        corpora = [corpus for corpus in corpora if corpus not in setup.OBSOLETE_CLTK_PACKAGES]
        # Check each corpus
        for required in corpora:
            # Building expected installation location
            location = str(
                root_location + '/' +
                required['type'] + '/' +
                required['name']
            )
            if not os.path.isdir(location):
                needed.append(required['name'])
        # Return needed packages
        if len(needed) > 0:
            return needed
        else:
            return False
