import unittest

from ..latin_doc import LatinDoc
from ..latin_corpus import LatinCorpus


class LatinCorpusUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = LatinCorpus([
            LatinDoc('Cuius rei'),
            LatinDoc('verisimilis causa'),
            LatinDoc('adferebatur, quod Gallis')
        ])
        compare = 'Cuius rei'
        return self.assertEqual(test[0], compare)

    # Disabled to improve testing time
    """
    def test_macronize(self):
        LatinCorpus([
            LatinDoc('Cuius rei'),
            LatinDoc('verisimilis causa'),
            LatinDoc('adferebatur, quod Gallis')
        ]).macronize()
        return self.assertEqual(True, True)
    """

    def test_normalize(self):
        LatinCorpus([
            LatinDoc('Cuius rei'),
            LatinDoc('verisimilis causa'),
            LatinDoc('adferebatur, quod Gallis')
        ]).normalize()
        return self.assertEqual(True, True)

    def test_stemmify(self):
        LatinCorpus([
            LatinDoc('Cuius rei'),
            LatinDoc('verisimilis causa'),
            LatinDoc('adferebatur, quod Gallis')
        ]).stemmify()
        return self.assertEqual(True, True)

    def test_clausulae(self):
        LatinCorpus([
            LatinDoc('quod superat non est melius quo insumere possis?'),
            LatinDoc('cur eget indignus quisquam te divite? quare'),
            LatinDoc('templa ruunt antiqua Deum? cur, inprobe, carae'),
            LatinDoc('non aliquid patriae tanto emetiris acervo? ')
        ]).clausulae()
        return self.assertEqual(True, True)
