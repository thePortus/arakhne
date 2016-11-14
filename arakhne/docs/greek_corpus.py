from .cltk_corpus import CLTKCorpus
from .greek_doc import GreekDoc


class GreekCorpus(CLTKCorpus):
    language = 'greek'
    doc = GreekDoc

    def normalize(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Normalizing text', counter)
            new_docs.append(doc.normalize())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def tag(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Lemmatizing', counter)
            new_docs.append(doc.tag())
        self.update(None, None)
        return new_docs
