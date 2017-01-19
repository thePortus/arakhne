import os
import csv

from .. import core


class CorpusIO:

    def __init__(self, corpus):
        self.corpus = corpus

    def csv(self, settings=None):
        return CSVFile(self.corpus, settings)


class BaseFile:
    filetype = 'base'
    settings = core.settings.FILES_ALL

    def __init__(self, corpus, settings=None):
        self.corpus = corpus
        if settings:
            self.settings.update(settings)

    def mk_path(self, path):
        # Return built absolute path if relative path sent
        if self.settings['path_type'] == 'relative':
            return os.path.join(os.getcwd(), path)
        return path

    def exists(self, path):
        return os.path.exists(path)

    def test_load(self, path):
        if not self.exists(path):
            raise OSError('No file found at that location')

    def test_save(self, path):
        if self.exists(path) and not self.settings['overwrite']:
            raise OSError('File already exists and overwrite not specified')


class CSVFile(BaseFile):
    filetype = 'csv'
    settings = core.settings.FILES_CSV

    def load(self, path):
        # Ensure path is absolute and check file
        path = self.mk_path(path)
        self.test_load(path)
        print('Loading', path)
        # Open the file
        with open(path, 'r+', encoding=self.settings['encoding']) as csv_file:
            # Create CSV reader object
            csv_reader = csv.DictReader(
                csv_file,
                delimiter=self.settings['delimiter'],
                quotechar=self.settings['quotechar'],
                dialect=self.settings['dialect']
            )
            # Build corpus list of metadata column names
            self.corpus.settings['meta_fields'] = []
            for fieldname in csv_reader.fieldnames:
                if fieldname != self.settings['text_col']:
                    self.corpus.settings['meta_fields'].append(fieldname)
            # Set corpus text column name
            self.corpus.settings['text_col'] = self.settings['text_col']
            for csv_record in csv_reader:
                text = None
                metadata = {}
                # Get text data
                try:
                    text = csv_record[self.settings['text_col']]
                except:
                    text = ''
                # Get metadata
                for meta_field in self.corpus.settings['meta_fields']:
                    metadata[meta_field] = csv_record[meta_field]
                # Build doc with text & metadata and append
                self.corpus = self.corpus.mk_doc(text, metadata=metadata)
        print("Corpus loaded successfully.")
        return self.corpus

    def save(self, path):
        # Ensure path is absolute and check file
        path = self.mk_path(path)
        self.test_save(path)
        print('Saving to', path)
        # Open file with specified settings
        with open(
            path,
            'w+',
            encoding=self.settings['encoding'],
            newline=self.settings['newline']
        ) as csv_file:
            # Build known field names from metadata fields and text col names
            fieldnames = []
            fieldnames.extend(self.corpus.settings['meta_fields'])
            fieldnames.append(self.corpus.settings['text_col'])
            # Prepare the csv dict writer with specified settings
            csv_writer = csv.DictWriter(
                csv_file,
                delimiter=self.settings['delimiter'],
                fieldnames=fieldnames,
                quotechar=self.settings['quotechar'],
                dialect=self.settings['dialect']
            )
            csv_writer.writeheader()
            for doc in self.corpus:
                export_record = {
                    self.corpus.settings['text_col']: doc,
                }
                for meta_field in self.corpus.settings['meta_fields']:
                    export_record[meta_field] = doc.metadata[meta_field]
                csv_writer.writerow(export_record)
        print('Corpus saved sucessfully.')
        # Return the corpus
        return self.corpus
