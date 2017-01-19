from .base_corpus import BaseCorpus as base
from .english_corpus import EnglishCorpus as english
from .latin_corpus import LatinCorpus as latin
from .greek_corpus import GreekCorpus as greek


class Corpus:

    def __init__(self, language=None, *args, **kwargs):
        self.language = language

    def make(self, docs=[], *args, **kwargs):
        if not self.language:
            return base(docs, args, kwargs)
        if self.language == 'english':
            return english(docs, args, kwargs)
        if self.language == 'latin':
            return latin(docs, args, kwargs)
        if self.language == 'greek':
            return greek(docs, args, kwargs)
