from .. import core
from .get_nltk import GetNLTK
from .get_cltk import GetCLTK


def Get(language):
    if core.languages.test_lang(language):
        if language == 'latin' or language == 'greek':
            return GetCLTK(language)
        if language == 'english':
            return GetNLTK(language)
