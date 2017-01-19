from .test_base_doc import AbstractTestDoc


class TestEnglishDoc(AbstractTestDoc):
    language = 'english'
    text = 'The\nquick bro-\nwn fox   jumped ov3r[sic] the lazy dog.'
