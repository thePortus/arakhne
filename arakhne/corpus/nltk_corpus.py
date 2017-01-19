from .base_corpus import BaseCorpus


class NLTKCorpus(BaseCorpus):

    def tokenize(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Tokenizing', counter)
            new_docs.append(doc.tokenize())
        self.update(None, None)
        return new_docs

    def lemmatize(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Lemmatizing', counter)
            new_docs.append(doc.lemmatize())
        self.update(None, None)
        return self.__class__(docs=new_docs)

    def ngrams(self, gram_size=3):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Compiling ngrams', counter)
            new_docs.append(doc.ngrams())
        self.update(None, None)
        return new_docs

    def skipgrams(self, gram_size=3, skip_size=1):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Compiling skipgrams', counter)
            new_docs.append(doc.skipgrams())
        self.update(None, None)
        return new_docs
