from .test_base_corpus import AbstractTestCorpus
from ...tests import EnglishFixtureLayer

class TestEnglishCorpus(AbstractTestCorpus):
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'
    language = 'english'
    layer = EnglishFixtureLayer
