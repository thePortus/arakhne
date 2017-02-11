from .test_base_corpus import AbstractTestCorpus

class TestEnglishCorpus(AbstractTestCorpus):
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'
    language = 'english'
