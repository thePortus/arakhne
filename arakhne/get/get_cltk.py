from cltk.corpus.utils.importer import CorpusImporter

from .get_base import GetBase


class GetCLTK(GetBase):
    pip_modules = ['cltk']

    def packages(self):
        if self.language != 'greek' and self.language != 'latin':
            raise NameError('Language must be Greek or Latin')
        print('Downloading', self.language, 'corpora...')
        try:
            corpus_importer = CorpusImporter(self.language)
            corpora_list = corpus_importer.list_corpora
            if len(corpora_list) == 0:
                print('Error: No corpora available for download at this time.')
            else:
                for corpus in corpora_list:
                    try:
                        corpus_importer.import_corpus(corpus)
                    # ignore unavailable corpora
                    except:
                        pass
        # If there is any problem creating the importer or listing corpora
        except:
            print('Error: Unknown error importing corpora.')
        print('Corpora imported successfully!')
        return True
