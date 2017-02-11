import re

from collections import UserString


class BaseDoc(UserString):
    language = None

    def __init__(self, data, metadata={}):
        super().__init__(str)
        self.data = data
        self.metadata = metadata

    def stringify(self):
        return str(self.data)

    def rm_lines(self):
        rexr = re.compile(r'\n+')
        # substituting single endlines for matching endline blocks
        clean_text = rexr.sub(' ', self.data)
        return self.__class__(
            clean_text
            .replace('-\n ', '').replace('- \n', '').replace('-\n', '')
            .replace(' - ', '').replace('- ', '').replace(' -', '')
            .replace('\n', ' '),
            self.metadata
        )

    def rm_nonchars(self):
        # If greek, only keep polytonic greek chars
        if self.language == 'greek':    # pragma: no cover
            clean_text = "".join(re.findall("([ʹ-Ϋά-ϡἀ-ᾯᾰ-῾ ])", self.data))
        # In all other cases, trim all but latin chars
        else:
            clean_text = "".join(re.findall("([A-Za-z ])", self.data))
        return self.__class__(
            clean_text,
            self.metadata
        )

    def rm_edits(self):
        return self.__class__(
            re.sub("\〚(.*?)\〛", "", re.sub("\{(.*?)\}", "", re.sub(
                "\((.*?)\)", "", re.sub("\<(.*?)\>", "", re.sub(
                    "\[(.*?)\]", "", self.data))))),
            self.metadata
        )

    def rm_spaces(self):
        # regex compiler for all whitespace blocks
        rexr = re.compile(r'\s+')
        # substituting single spaces for matching whitespace blocks
        clean_text = rexr.sub(' ', self.data)
        return self.__class__(
            clean_text.strip(),
            self.metadata
        )

    def re_search(self, pattern):
        # Converting pattern to regex
        pattern = re.compile(pattern)
        if pattern.search(self.data):
            return True
        else:
            return False

    def rm_stopwords(self, stoplist=[]):
        filtered_words = []
        # converts text to list of words with NLTK tokenizer
        tokens = self.data.split()
        # loop through each word, if not in stoplist, append
        for word in tokens:
            not_found = True
            for stopword in stoplist:
                if str(word) == str(stopword):
                    not_found = False
            if not_found:
                filtered_words.append(word)
        # return rejoined word
        return self.__class__(
            " ".join(filtered_words),
            self.metadata
        )
