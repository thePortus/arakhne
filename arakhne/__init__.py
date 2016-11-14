from .docs import Docs


class Arakhne:

    def __init__(self, language=None, *args, **kwargs):
        self.title = ''
        self.settings = {}
        self.language = language
        # Store all passed kwargs in settings
        if kwargs is not None:
            self.settings.update(kwargs)
        # Copy title property if passed
        if 'title' in kwargs:
            self.title = kwargs['title']
        self.corpus = Docs(language).corpus
