""" Access Doc methods at the corpus level and analyze en masse """

from .base_corpus import BaseCorpus as base
from .english_corpus import EnglishCorpus as english
from .latin_corpus import LatinCorpus as latin
from .greek_corpus import GreekCorpus as greek

__author__ = 'David J. Thomas <dave.a.base@gmail.com>'
__license__ = 'MIT License. See LICENSE.'


class Corpus:

    def __init__(self, language=None, *args, **kwargs):
        self.language = language
        # ADD VALIDATE AND INSTALL STUFF HERE

    def make(self, docs=[], *args, **kwargs):
        if not self.language:
            return base(docs, args, kwargs)
        if self.language == 'english':
            return english(docs, args, kwargs)
        if self.language == 'latin':
            return latin(docs, args, kwargs)
        if self.language == 'greek':
            return greek(docs, args, kwargs)
