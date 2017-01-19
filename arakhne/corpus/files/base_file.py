import os
import sys

from arakhne.settings import Defaults


class BaseFile:
    filetype = 'base'
    settings = Defaults.FILES_ALL

    def __init__(self, corpus, settings=None):
        self.corpus = corpus
        if settings:
            self.settings.update(settings)

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
        message += str(prefix_msg) + " " + str(counter)
        message += " " + str(postscript_msg)
        sys.stdout.write(message)
        return True

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
