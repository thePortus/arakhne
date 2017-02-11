from .cltk_doc import CLTKDoc
from cltk.prosody.latin.clausulae_analysis import Clausulae
from cltk.prosody.latin.macronizer import Macronizer
from cltk.stem.latin.j_v import JVReplacer
from cltk.stem.latin.stem import Stemmer


class LatinDoc(CLTKDoc):
    language = 'latin'

    def macronize(self, mode='tag_ngram_123_backoff'):  # pragma: no cover
        mode = mode.lower()
        if (
            mode != 'tag_ngram_123_backoff' and
            mode != 'tag_tng' and
            mode != 'tag_crf'
        ):
            return False
        return self.__class__(
            Macronizer(tagger=mode).macronize_text(self.data),
            self.metadata
        )

    def normalize(self):
        return self.__class__(
            JVReplacer().replace(self.data),
            self.metadata
        )

    def stemmify(self):
        return self.__class__(
            Stemmer().stem(self.data.lower()),
            self.metadata
        )

    def clausulae(self):    # pragma: no cover
        return Clausulae().clausulae_analysis(self.data)
