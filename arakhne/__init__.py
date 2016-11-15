from .docs import Docs


class Arakhne:

    def __init__(self, language=None, *args, **kwargs):
        self.title = ''
        self.settings = {}
        self.language = language
        self.downloader = CorporaDownloader(self.language)
        self.corpus = None
        # Store all passed kwargs in settings
        if kwargs is not None:
            self.settings.update(kwargs)
        # Copy title property if passed
        if 'title' in kwargs:
            self.title = kwargs['title']
        self.corpus = Docs(language).corpus


class CorporaDownloader:

    def __init__(self, language):
        self.language = language

    def nltk(self):
        import nltk
        nltk.download()
        return True

    def cltk(self):
        from cltk.corpus.utils.importer import CorpusImporter
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
