import re

from collections import UserString


class BaseDoc(UserString):
    language = None

    def __init__(self, data, metadata={}, stats={}):
        super().__init__(str)
        self.data = data
        self.metadata = metadata
        self.stats = stats

    def stringify(self):
        return str(self.data)

    def rm_lines(self):
        return self.__class__(
            self.data
                .replace('-\n ', '').replace('- \n', '').replace('-\n', '')
                .replace(' - ', '').replace('- ', '').replace(' -', '')
                .replace('\n', ' '),
            self.metadata,
            self.stats
        )

    def rm_nonchar(self):
        # If greek, only keep polytonic greek chars
        if self.language == 'greek':
            clean_text = "".join(re.findall("([ʹ-Ϋά-ϡἀ-ᾯᾰ-῾ ])", self.data))
        # In all other cases, trim all but latin chars
        else:
            clean_text = "".join(re.findall("([A-Za-z ])", self.data))
        return self.__class__(
            clean_text,
            self.metadata,
            self.stats
        )

    def rm_edits(self):
        return self.__class__(
            re.sub("\〚(.*?)\〛", "", re.sub("\{(.*?)\}", "", re.sub(
                "\((.*?)\)", "", re.sub("\<(.*?)\>", "", re.sub(
                    "\[(.*?)\]", "", self.data))))),
            self.metadata,
            self.stats
        )

    def rm_spaces(self):
        # regex compiler for all whitespace blocks
        rexr = re.compile(r'\s+')
        # substituting single spaces for matching whitespace blocks
        clean_text = rexr.sub(' ', self.data)
        return self.__class__(
            clean_text.strip(),
            self.metadata,
            self.stats
        )

    def re_search(self, pattern):
        # Converting pattern to regex
        pattern = re.compile(pattern)
        if pattern.search(self.data):
            return True
        else:
            return False
