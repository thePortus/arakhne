from nltk.text import Text
from cltk.tokenize.word import nltk_tokenize_words
from cltk.tokenize.sentence import TokenizeSentence
from cltk.stem.lemma import LemmaReplacer
from cltk.prosody.greek.scanner import Scansion as GreekScansion
from cltk.prosody.latin.scanner import Scansion as LatinScansion
from cltk.text_reuse.levenshtein import Levenshtein
from cltk.text_reuse.comparison import long_substring, minhash
from cltk.tag import ner
from cltk.utils.frequency import Frequency

from .nltk_doc import NLTKDoc


class CLTKDoc(NLTKDoc):

    def tokenize(self, mode='word'):
        if mode == 'sentence':
            return TokenizeSentence(
                self.language
            ).tokenize_sentences(self.data)
        else:
            return nltk_tokenize_words(self.data)

    def lemmatize(self, return_string=True, return_raw=False):  # pragma: no cover
        return self.__class__(
            data=LemmaReplacer(
                self.language
            ).lemmatize(
                self.data.lower(),
                return_string=return_string,
                return_raw=return_raw
            ),
            metadata=self.metadata
        )

    def scansion(self):     # pragma: no cover
        if self.language == 'greek':
            return GreekScansion().scan_text(self.data)
        if self.language == 'latin':
            return LatinScansion().scan_text(self.data)

    def entities(self, lemmatize=False, unique=False):
        entity_list = []
        # filtering non-entities
        for result in ner.tag_ner(
            self.language,
            input_text=self.data,
            output_type=list
        ):
            # appending if item flagged as entity in tuple[1]
            try:
                if result[1] == 'Entity':
                    entity_list.append(result[0])
            # do nothing if 'Entity' not specified
            except:
                pass
            # removing duplicate entities if unique option specified
        if unique:
            entity_list = list(set(entity_list))
        # lemmatizing entities if option has been specified
        if lemmatize:
            entity_list = LemmaReplacer(self.language).lemmatize(
                entity_list,
                return_string=False,
                return_raw=False
            )
        return entity_list

    def compare_levenshtein(self, other_text):
        return Levenshtein().ratio(self.data, other_text)

    def compare_longest_common_substring(self, other_text):
        return long_substring(self.data, other_text)

    def compare_minhash(self, other_text):
        return minhash(self.data, other_text)

    def word_count(self, word=None, mode='cltk'):
        if mode == 'nltk':
            counts = dict(Text(self.tokenize()).vocab())
        else:
            counts = Frequency().counter_from_str(self.data)
        # If a single word was specified, only return that frequency
        if word:
            return counts[word]
        return counts
