from .cltk_corpus import CLTKCorpus
from .latin_doc import LatinDoc


class LatinCorpus(CLTKCorpus):
    language = 'latin'
    doc = LatinDoc

    def macronize(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Macronizing vowels', counter)
            new_docs.append(doc.macronize())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def jv_replace(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Normalizing j/i and v/u', counter)
            new_docs.append(doc.jv_replace())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def stemmify(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Stemmifying', counter)
            new_docs.append(doc.stemmify())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def clausulae(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Analyzing clausulae', counter)
            new_docs.append(doc.clausulae())
        self.update(None, None)
        return new_docs