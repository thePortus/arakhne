from .english_corpus import EnglishCorpus


class CLTKCorpus(EnglishCorpus):

    def lemmatize(self, return_string=True, return_raw=False):  # pragma: no cover
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Lemmatizing', counter)
            new_doc = doc.lemmatize(
                return_string=return_string,
                return_raw=return_raw,
            )
            new_docs.append(new_doc)
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def scansion(self):     # pragma: no cover
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Performing Scansion', counter)
            new_docs.append(doc.scansion())
        self.update(None, None)
        return new_docs

    def entities(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Scanning entities', counter)
            new_docs.append(doc.entities())
        self.update(None, None)
        return new_docs
