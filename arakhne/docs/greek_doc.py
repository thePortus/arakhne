from .cltk_doc import CLTKDoc
from cltk.corpus.utils.formatter import cltk_normalize
from cltk.tag.pos import POSTag


class GreekDoc(CLTKDoc):
    language = 'greek'

    def normalize(self):
        return self.__class__(
            cltk_normalize(str(self.data)),
            self.metadata,
            self.stats
        )

    def tag(self, mode='123'):
        tagger = POSTag(self.language)
        mode = mode.lower()
        if mode != '123' and mode != 'tnt' and mode != 'crf':
            print('Error: invalid part of speech tagging mode specified.')
            return False
        elif mode == '123':
            return tagger.tag_ngram_123_backoff(self.data)
        elif mode == 'tnt':
            return tagger.tag_tnt(self.data)
        else:
            return tagger.tag_crf(self.data)
