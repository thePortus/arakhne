from .test_base_doc import AbstractTestDoc


class TestLatinDoc(AbstractTestDoc):
    text = 'Omnia gallia\nin tres part-\nes divisa est.'
    language = 'latin'

    def test_normalize(self):
        self.ready()
        test = self.doc.normalize()
        compare = 'Omnia gallia\nin tres part-\nes diuisa est.'
        return self.assertEqual(test, compare)

    def test_stemmify(self):
        self.ready()
        test = self.doc.stemmify()
        compare = 'omn gallia\nin tr part-\n divis est. '
        return self.assertEqual(test, compare)
