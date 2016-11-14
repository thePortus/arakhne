import os
import csv
import sys
from collections import UserList

from .base_doc import BaseDoc


class BaseCorpus(UserList):
    language = None
    doc = BaseDoc
    settings = {}

    def __init__(self, docs=None, *args, **kwargs):
        super().__init__()
        self.save = CorpusExporter(self)
        self.load = CorpusImporter(self)
        # Store kwargs in settings dict
        self.settings = {
            'meta_fields': [],
            'text_col': None
        }
        if kwargs is not None:
            self.settings.update(kwargs)
        if docs:
            self.data = docs

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

    def rm_nonchar(self):
        new_docs = []
        counter = 0
        for doc in self.data:
            counter += 1
            self.update('Removing non-characters', counter)
            new_docs.append(doc.rm_nonchar())
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

    def mk_doc(self, doc, metadata={}):
        self.append(self.doc(doc, metadata=metadata))
        return self


class CorpusImporter:

    def __init__(self, corpus, **kwargs):
        self.corpus = corpus
        # Set default settings
        self.settings = {
            'path_type': 'relative',
            'newline': '',
            'encoding': 'utf-8',
            'delimiter': ',',
            'quotechar': '"',
            'dialect': 'excel',
        }
        # Update settings with passed keyword args
        if kwargs is not None:
            self.settings.update(kwargs)

    def csv(self, path, **kwargs):
        # Default settings
        settings = {
            'path_type': 'relative',
            'encoding': 'utf-8',
            'delimiter': ',',
            'quotechar': '"',
            'dialect': 'excel',
            'text_col': 'text'
        }
        # Update default settings with keyword args
        if kwargs is not None:
            settings.update(kwargs)
        # Build absolute path if relative path sent
        if settings['path_type'] == 'relative':
            path = os.path.join(os.getcwd(), path)
        if not os.path.exists(path):
            raise OSError('No file found at that location')
        print('Loading', path)
        # Open the file
        with open(path, 'r+', encoding=settings['encoding']) as csv_file:
            # Create CSV reader object
            csv_reader = csv.DictReader(
                csv_file,
                delimiter=settings['delimiter'],
                quotechar=settings['quotechar'],
                dialect=settings['dialect']
            )
            # Build corpus list of metadata column names
            for fieldname in csv_reader.fieldnames:
                if fieldname != settings['text_col']:
                    self.corpus.settings['meta_fields'].append(fieldname)
            # Set corpus text column name
            self.corpus.settings['text_col'] = settings['text_col']
            for csv_record in csv_reader:
                text = None
                metadata = {}
                # Get text data
                try:
                    text = csv_record[settings['text_col']]
                except:
                    text = ''
                # Get metadata
                for meta_field in self.corpus.settings['meta_fields']:
                    metadata[meta_field] = csv_record[meta_field]
                # Build doc with text & metadata and append
                self.corpus = self.corpus.mk_doc(text, metadata=metadata)
        return self.corpus


class CorpusExporter:

    def __init__(self, corpus, **kwargs):
        self.corpus = corpus
        # Set default settings
        self.settings = {
            'path_type': 'relative',
            'newline': '',
            'encoding': 'utf-8',
            'delimiter': ',',
            'quotechar': '"',
            'dialect': 'excel',
            'overwrite': True,
        }
        # Update settings with passed keyword args
        if kwargs is not None:
            self.settings.update(kwargs)

    def csv(self, path, **kwargs):
        settings = self.settings
        # Update local settings with any passed keyword args
        if kwargs is not None:
            settings.update(kwargs)
        # Build absolute path if relative path sent
        if self.settings['path_type'] == 'relative':
            path = os.path.join(os.getcwd(), path)
        if os.path.exists(path) and not self.settings['overwrite']:
            raise OSError('File already exists and overwrite not specified')
        print('Saving to', path)
        with open(
            path,
            'w+',
            encoding=settings['encoding'],
            newline=settings['newline']
        ) as csv_file:
            fieldnames = []
            fieldnames.extend(self.corpus.settings['meta_fields'])
            fieldnames.append(self.corpus.settings['text_col'])
            csv_writer = csv.DictWriter(
                csv_file,
                delimiter=settings['delimiter'],
                fieldnames=fieldnames,
                quotechar=settings['quotechar'],
                dialect=settings['dialect']
            )
            csv_writer.writeheader()
            for doc in self.corpus:
                export_record = {
                    self.corpus.settings['text_col']: doc,
                }
                for meta_field in self.corpus.settings['meta_fields']:
                    export_record[meta_field] = doc.metadata[meta_field]
                csv_writer.writerow(export_record)
        # Return the corpus
        return self.corpus
