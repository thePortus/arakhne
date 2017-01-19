from .test_base_doc import AbstractTestDoc


class TestCLTKDoc(AbstractTestDoc):
    text = 'Omnia gallia\nin tres part-\nes divisa est.'
    language = 'latin'

    def test_tokenize(self):
        self.setup()
        test = len(self.doc.tokenize())
        compare = 9
        return self.assertEqual(test, compare)

    def test_tokenize_sentence(self):
        self.setup()
        test = len(self.doc.tokenize(mode='sentence'))
        compare = 1
        return self.assertEqual(test, compare)

    def test_entities(self):
        self.setup()
        test = self.doc.entities()
        compare = []
        return self.assertEqual(test, compare)

    """
    def test_lemmatize(self):
        self.setup()
        test = len(self.doc.lemmatize())
        compare = 43
        return self.assertEqual(test, compare)
    """

    """
    def test_scansion(self):
        self.setup()
        self.doc.data = 'Arma virumque cano Troiae qui primus ab oris'
        test = self.doc.scansion()
        compare = ['¯˘˘¯˘˘˘˘˘¯˘˘˘˘˘x']
        return self.assertEqual(test, compare)
    """

    def test_compare_levenshtein(self):
        self.setup()
        alt_text = 'Omnia gallia in tres partes divisa est'
        test = self.doc.compare_levenshtein(alt_text)
        compare = 0.94
        return self.assertEqual(test, compare)

    def test_compare_longest_common_substring(self):
        self.setup()
        alt_text = 'Omnia gallia in tres partes divisa est'
        test = self.doc.compare_longest_common_substring(alt_text)
        compare = 'es divisa est'
        return self.assertEqual(test, compare)

    def test_compare_minhash(self):
        self.setup()
        alt_text = 'Omnia gallia in tres partes divisa est'
        test = self.doc.compare_minhash(alt_text)
        compare = 0.7142857142857143
        return self.assertEqual(test, compare)

    def test_word_count(self):
        self.setup()
        test = self.doc.word_count()['Omnia']
        compare = 1
        return self.assertEqual(test, compare)

    def test_word_count_specific(self):
        self.setup()
        test = self.doc.word_count('Omnia')
        compare = 1
        return self.assertEqual(test, compare)

    def test_word_count_nltk_mode(self):
        self.setup()
        test = self.doc.word_count('Omnia', mode='nltk')
        compare = 1
        return self.assertEqual(test, compare)
