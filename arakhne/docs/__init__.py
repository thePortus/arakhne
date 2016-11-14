from .base_corpus import BaseCorpus


class Docs:

    def __init__(self, language=None, *args, **kwargs):
        self.language = language
        self.corpus = None
        if not self.language:
            self.corpus = BaseCorpus()
        elif self.language == 'english':
            from .english_corpus import EnglishCorpus
            self.corpus = EnglishCorpus()
        elif self.language == 'greek':
            from .greek_corpus import GreekCorpus
            self.corpus = GreekCorpus()
        elif self.language == 'latin':
            from .latin_corpus import LatinCorpus
            self.corpus = LatinCorpus()
        else:
            raise TypeError('Invalid language specified')
