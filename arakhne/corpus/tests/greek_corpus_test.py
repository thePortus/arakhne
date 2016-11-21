"""
import unittest

from ..greek_doc import GreekDoc
from ..greek_corpus import GreekCorpus


class GreekCorpusUnitTest(unittest.TestCase):

    def test_functionality(self):
        test = GreekCorpus([
            GreekDoc('ὁ δὲ Πειραιεὺς'),
            GreekDoc('δῆμος μὲν ἦν ἐκ παλαιοῦ,'),
            GreekDoc('πρότερον δὲ')
        ])
        compare = 'ὁ δὲ Πειραιεὺς'
        return self.assertEqual(test[0], compare)

    def test_tlgu_cleanup(self):
        GreekCorpus([
            GreekDoc('ὁ δὲ Πειραιεὺς'),
            GreekDoc('δῆμος μὲν ἦν ἐκ παλαιοῦ,'),
            GreekDoc('πρότερον δὲ')
        ]).lemmatize()
        return self.assertEqual(True, True)

    def test_normalize(self):
        GreekCorpus([
            GreekDoc('ὁ δὲ Πειραιεὺς'),
            GreekDoc('δῆμος μὲν ἦν ἐκ παλαιοῦ,'),
            GreekDoc('πρότερον δὲ')
        ]).normalize()
        return self.assertEqual(True, True)

    def test_tag(self):
        GreekCorpus([
            GreekDoc('ὁ δὲ Πειραιεὺς'),
            GreekDoc('δῆμος μὲν ἦν ἐκ παλαιοῦ,'),
            GreekDoc('πρότερον δὲ')
        ]).tag()
        return self.assertEqual(True, True)

    def test_lemmatize(self):
        GreekCorpus([
            GreekDoc('ὁ δὲ Πειραιεὺς'),
            GreekDoc('δῆμος μὲν ἦν ἐκ παλαιοῦ,'),
            GreekDoc('πρότερον δὲ')
        ]).lemmatize()
        return self.assertEqual(True, True)

    def test_entities(self):
        GreekCorpus([
            GreekDoc('ὁ δὲ Πειραιεὺς'),
            GreekDoc('δῆμος μὲν ἦν ἐκ παλαιοῦ,'),
            GreekDoc('πρότερον δὲ')
        ]).entities()
        return self.assertEqual(True, True)

    def test_scansion(self):
        GreekCorpus([
            GreekDoc('βὰν δὲ δι᾽ αἰθούσης,  ἔνθα σφίσι πότνια μήτηρ'),
            GreekDoc('ἧστο παρὰ σταθμὸν τέγεος πύκα ποιητοῖο'),
            GreekDoc('παῖδ᾽ ὑπὸ κόλπῳ ἔχουσα, νέον θάλος: αἳ δὲ πὰρ αὐτὴν'),
            GreekDoc('ἔδραμον: ἣ δ᾽ ἄρ᾽ ἐπ᾽ οὐδὸν ἔβη ποσὶ καὶ ῥα μελάθρου'),
            GreekDoc('κῦρε κάρη, πλῆσεν δὲ θύρας σέλαος θείοιο.')
        ]).scansion()
        return self.assertEqual(True, True)
"""
