from .test_base_doc import AbstractTestDoc


class TestGreekDoc(AbstractTestDoc):
    text = 'Ἡροδότου Ἁλικαρνησσέος ἱστορίης ἀπόδεξις ἥδε'
    language = 'greek'

    def test_normalize(self):
        self.ready()
        test = self.doc.normalize()
        compare = 'Ἡροδότου Ἁλικαρνησσέος ἱστορίης ἀπόδεξις ἥδε'
        return self.assertEqual(test, compare)

    def test_tlgu_cleanup(self):
        self.ready()
        test = self.doc.tlgu_cleanup()
        compare = 'Ἡροδότου Ἁλικαρνησσέος ἱστορίης ἀπόδεξις ἥδε'
        return self.assertEqual(test, compare)

    def test_tag_123(self):
        self.ready()
        test = len(self.doc.tag(mode='123'))
        compare = 5
        return self.assertEqual(test, compare)

    def test_tag_tnt(self):
        self.ready()
        test = len(self.doc.tag(mode='tnt'))
        compare = 5
        return self.assertEqual(test, compare)

    def test_tag_invalid(self):
        self.ready()
        with self.assertRaises(Exception):
            self.doc.tag(mode='fake')
        return True
