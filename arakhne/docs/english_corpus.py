from .nltk_corpus import NLTKCorpus
from .english_doc import EnglishDoc


class EnglishCorpus(NLTKCorpus):
    language = 'english'
    doc = EnglishDoc
