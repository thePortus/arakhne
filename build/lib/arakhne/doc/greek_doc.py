from .cltk_doc import CLTKDoc
from cltk.corpus.utils.formatter import cltk_normalize
from cltk.tag.pos import POSTag
from cltk.corpus.utils.formatter import tlg_plaintext_cleanup


class GreekDoc(CLTKDoc):
    language = 'greek'

    def normalize(self):
        return self.__class__(
            cltk_normalize(str(self.data)),
            self.metadata
        )

    def tlgu_cleanup(self, rm_punctuation=True, rm_periods=False):
        return self.__class__(
            data=tlg_plaintext_cleanup(
                self.data, rm_punctuation=rm_punctuation, rm_periods=rm_periods
            ),
            metadata=self.metadata
        )

    def tag(self, mode='123'):
        tagger = POSTag(self.language)
        mode = mode.lower()
        if mode != '123' and mode != 'tnt':
            raise Exception(
                'Invalid part of speech tagging mode specified.'
            )
        elif mode == '123':
            return tagger.tag_ngram_123_backoff(self.data)
        elif mode == 'tnt':
            return tagger.tag_tnt(self.data)
