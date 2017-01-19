from .base_file import BaseFile
from .csv_file import CSVFile


class CorpusIO:

    def __init__(self, corpus):
        self.corpus = corpus

    def csv(self, settings=None):
        return CSVFile(corpus=self.corpus, settings=settings)
