from .cltk_corpus import CLTKCorpus


class GreekCorpus(CLTKCorpus):
    language = 'greek'

    def normalize(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Normalizing text', counter)
            new_docs.append(doc.normalize())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def tlgu_cleanup(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Performing TLGU cleanup', counter)
            new_docs.append(doc.tlgu_cleanup())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def tag(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Tagging parts of speech', counter)
            new_docs.append(doc.tag())
        self.update(None, None)
        return new_docs
