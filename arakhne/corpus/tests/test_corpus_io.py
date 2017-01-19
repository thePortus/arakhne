import unittest
import os

from .. import Corpus
from arakhne.common import get_env_variable


class AbstractTestIO(unittest.TestCase):
    fixtures = get_env_variable('ARAKHNE_TEST_FIXTURES')
    file_in = os.path.join(fixtures, 'input_english.csv')
    file_out = os.path.join(fixtures, 'output.csv')
    language = 'english'
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'

    def setup(self):
        self.corpus = Corpus(self.language).make().mk_doc(self.text)


class TestCSVIO(AbstractTestIO):

    def test_load(self):
        self.setup()
        self.corpus.csv().load(self.file_in)
        return True
