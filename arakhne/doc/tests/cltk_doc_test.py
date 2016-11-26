"""
import unittest

from .. import Doc


class CLTKDocUnitTest(unittest.TestCase):
    test = Doc('latin').make(
        'Cuius rei verisimilis causa adferebatur'
    )

    def test_tokenize(self):
        compare = ['Cuius', 'rei', 'verisimilis', 'causa', 'adferebatur']
        test = self.test.tokenize()
        return self.assertEqual(test, compare)

    def test_entities(self):
        compare = ['Cuius']
        test = self.test.entities()
        return self.assertEqual(test, compare)

    def test_word_count(self):
        compare = 1
        test = self.test.word_count()['adferebatur']
        return self.assertEqual(test, compare)

    # def test_lemmatize(self):
    #    compare = 'qui1 redeo verisimilis causa affero'
    #     test = self.test.lemmatize()
    #     return self.assertEqual(test, compare)

    def test_scansion(self):
        compare = 'rancidum aprum antiqui laudabant, non quia nasus'
        test = Doc('latin').make(
            'rancidum aprum antiqui laudabant, non quia nasus'
        )
        return self.assertEqual(test, compare)

    def test_compare_levenshtein(self):
        string_a = Doc('latin').make(
            'rancidum aprum antiqui laudabant, non quia nasus'
        )
        string_b = Doc('latin').make(
            'illis nullus erat, sed, credo, hac mente, quod hospes'
        )
        compare = 0.36
        test = string_a.compare_levenshtein(string_b)
        return self.assertEqual(test, compare)

    def test_compare_longest_common_substring(self):
        string_a = Doc('latin').make(
            'rancidum aprum antiqui laudabant, non quia nasus'
        )
        string_b = Doc('latin').make(
            'illis nullus erat, sed, credo, hac mente, quod hospes'
        )
        compare = 't,'
        test = string_a.compare_longest_common_substring(string_b)
        return self.assertEqual(test, compare)

    def test_compare_minhash(self):
        string_a = Doc('latin').make(
            'rancidum aprum antiqui laudabant, non quia nasus'
        )
        string_b = Doc('latin').make(
            'illis nullus erat, sed, credo, hac mente, quod hospes'
        )
        compare = 0.02197802197802198
        test = string_a.compare_minhash(string_b)
        return self.assertEqual(test, compare)
"""
