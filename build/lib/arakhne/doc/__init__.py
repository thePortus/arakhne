from .base_doc import BaseDoc as base
from .english_doc import EnglishDoc as english
from .latin_doc import LatinDoc as latin
from .greek_doc import GreekDoc as greek


class Doc:

    def __init__(self, language=None):
        self.language = language

    def make(self, text, metadata={}):
        if not self.language:
            return base(text, metadata)
        if self.language == 'english':
            return english(text, metadata)
        if self.language == 'latin':
            return latin(text, metadata)
        if self.language == 'greek':
            return greek(text, metadata)
