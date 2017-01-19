import sys
from collections import UserList

from .. import core
from ..doc import Doc
from .corpus_io import CorpusIO
from ..get import Get


class BaseCorpus(UserList):
    language = None
    settings = {}

    def __init__(self, docs=None, *args, **kwargs):
        super().__init__()
        # Set defaults and update with passed kwargs
        self.settings = core.settings.CORPORA_ALL
        if kwargs is not None:
            self.settings.update(kwargs)
        if docs:
            self.data = docs
        # Create module & trainer importer for language
        self.get = Get(self.language)

    @property
    def len(self):
        return len(self)

    def update(
        self,
        prefix_msg,
        counter,
        postscript_msg='',
    ):
        if not prefix_msg and not counter:
            sys.stdout.write('\n')
            return True
        message = '\r'
        counter_max = self.len
        message += str(prefix_msg) + " " + str(counter) + "/"
        message += str(counter_max) + " - "
        message += str(round((counter / counter_max) * 100, 2)) + "%"
        message += " " + str(postscript_msg)
        sys.stdout.write(message)
        return True

    def rm_lines(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Removing endlines', counter)
            new_docs.append(doc.rm_lines())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def rm_nonchars(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Removing non-characters', counter)
            new_docs.append(doc.rm_nonchars())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def rm_edits(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Removing editorials', counter)
            new_docs.append(doc.rm_edits())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def rm_spaces(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Collapsing spaces', counter)
            new_docs.append(doc.rm_spaces())
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def rm_stopwords(self, stoplist=[]):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Filtering stopwords', counter)
            new_docs.append(doc.rm_stopwords(stoplist))
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def re_search(self, pattern):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Searching for ' + str(pattern), counter)
            # Only appending docs that match the pattern
            if doc.re_search(pattern):
                new_docs.append(doc)
        self.update(None, None)
        return self.__class__(new_docs, **self.settings)

    def mk_doc(self, text, metadata={}):
        self.append(Doc(self.language).make(text, metadata=metadata))
        return self

    def csv(self, settings=None):
        return CorpusIO(self).csv(settings=settings)
