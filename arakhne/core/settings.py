from ..corpus import BaseCorpus, EnglishCorpus, LatinCorpus, GreekCorpus
from ..doc import BaseDoc, EnglishDoc, LatinDoc, GreekDoc

SUPPORTED_LANGS = [None, 'english', 'latin', 'greek']

LANG_OBJECTS = {
    None: {
        'doc': BaseDoc,
        'corpus': BaseCorpus
    },
    'english': {
        'doc': EnglishDoc,
        'corpus': EnglishCorpus
    },
    'latin': {
        'doc': LatinDoc,
        'corpus': LatinCorpus
    },
    'greek': {
        'doc': GreekDoc,
        'corpus': GreekCorpus
    }
}
