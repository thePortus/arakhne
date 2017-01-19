from .test_base_doc import AbstractTestDoc


class TestGreekDoc(AbstractTestDoc):
    text = 'Ἡροδότου Ἁλικαρνησσέος ἱστορίης ἀπόδεξις ἥδε'
    language = 'greek'

    def test_normalize(self):
        self.setup()
        test = self.doc.normalize()
        compare = 'Ἡροδότου Ἁλικαρνησσέος ἱστορίης ἀπόδεξις ἥδε'
        return self.assertEqual(test, compare)

    def test_tlgu_cleanup(self):
        self.setup()
        test = self.doc.tlgu_cleanup()
        compare = 'Ἡροδότου Ἁλικαρνησσέος ἱστορίης ἀπόδεξις ἥδε'
        return self.assertEqual(test, compare)

    def test_tag_123(self):
        self.setup()
        test = len(self.doc.tag(mode='123'))
        compare = 5
        return self.assertEqual(test, compare)

    def test_tag_tnt(self):
        self.setup()
        test = len(self.doc.tag(mode='tnt'))
        compare = 5
        return self.assertEqual(test, compare)

    def test_tag_invalid(self):
        self.setup()
        with self.assertRaises(Exception):
            self.doc.tag(mode='fake')
        return True
