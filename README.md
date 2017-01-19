# Arakhne Text Loom:

<small>Corpus Analytics for English, Latin, and Greek</small>

*By David J. Thomas, [thePortus.com](http://theportus.com/)*

---

![Travis CI Badge](https://travis-ci.org/thePortus/arakhne.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/thePortus/arakhne/badge.svg?branch=master)](https://coveralls.io/github/thePortus/arakhne?branch=master)

---

[Click here to see an example of Arakhne in practice](https://github.com/thePortus/dio/blob/master/arakhne_dio.ipynb)

---

Scrub and analyze CSVs or folders of English, Latin and Greek text data, working with corpora just like a list of documents!

Powered by the [NLTK](http://www.nltk.org/) and [CLTK](https://github.com/cltk/cltk) modules, Arakhne attemps to make the scrubbing and analysis of mass volumes of texts accessible to the Ancient Scholar with minimal Python training. The goal of Arakhne is to allow the user to perform the greatest number of changes in the fewest number of commands possible, all while maintaining semantic clarity.

My students have great analytical questions, but limited programming experience. They needed to get on with the business of scholarly analysis. So, I created Arakhne so that they could load, scrub, analyze, and save a large corpus of texts in a few short lines of code. Since then, it has grown in scope considerably.

The [Natural Language Toolkit](https://nltk.org) has enabled modern text analysis for some years now. Recently, the amazing [Classical Language Toolkit, or CLTK](http://cltk.org), has brought machine language processing to ancient studies. The CLTK library powers the majority of operations behind this module. However, CLTK operations focus on analyzing single bits of text (or other data focused on a single 'document').

As Latinists well know, a *textus* is literally 'something woven.' With Arakhne, you can unravel a corpus and explore the documents, words, people, and places that bind the documents together.

---

System Requirements:

* Basic Corpus Scrubbing: Windows / OSX / Linux
* Language Specific Operations: OSX / Linux **ONLY**

Only Python 3 is supported at this time.

---

## Contents
* [Installation](#installation)
* [Basic Usage](#basic-usage)
* [Scrubbing](#scrubbing)
* [Lemmatizing, Filtering, and Stopwords](#lemmatizing-filtering-and-stopwords)
* [License](#license)

---

## Installation

``` python
pip install arakhne
```

---

[Click here to see an example of Arakhne in practice](https://github.com/thePortus/dio/blob/master/arakhne_dio.ipynb)

---

## Basic Usage
``` python
from arakhne import Arakhne

# Load a corpus from a CSV
cassius_dio = Arakhne('greek').csv().load('dio_raw.csv')
# Perform on operation on the entire corpus
cassius_dio = cassius_dio.rm_lines()
# Save a corpus
cassius_dio.csv().save('dio_raw_backup.csv')

# Or load, transform, and save, all in one line
Arakhne('greek').csv().load('dio_raw.csv').rm_lines().csv().save('dio_new.csv')
```

---

## Scrubbing
``` python
# Removes all endline characters
cassius_dio = cassius_dio.rm_lines()
# Removes texts between editorial marks, e.g. []{}()<>, etc.
cassius_dio = cassius_dio.rm_edits()
# Removes characters not belonging to the specified language
cassius_dio = cassius_dio.rm_nonchars()
# Normalize certain Greek accent character encoding issues
cassius_dio = cassius_dio.normalize()
# Removes redundant whitespace (often created by the above operations)
cassius_dio = cassius_dio.rm_spaces()

# Or, chain them together to perform multiple operations
cassius_dio = cassius_dio.rm_lines().rm_edits().rm_nonchars().rm_spaces()
```

---

## Lemmatizing, Filtering, and Stopwords

``` python
# Create a lemmatized version for indexing purposes
lemmatized_dio = cassius_dio.lemmatize()

# Create a filtered corpus containing only passages matching a Regex pattern
filtered_dio = stopped_dio.re_search('πολλοί')

# Pass a list to remove specified words
stopped_dio = cassius_dio.rm_stopwords(['ὁ', 'δὲ', 'ὅτι'])

# Using language default stopwords
stopped_dio = cassius_dio.rm_stopwords()

# Or using a specified plaintext list of stop phrases
stopped_dio = cassius_dio.set_stopwords('stopwords_greek.txt').rm_stopwords()
```

---

## Tagging and Named Entity Recognition

``` python

# Returns list of lists, each containing tuples of the word and part of speech
tagged_dio = scrubbed_dio.tag()

# Returns list of lists, each containing strings with entity names
entities_dio = scrubbed_dio.entities()
```

---

### License
```
The MIT License (MIT)

Copyright (c) 2016 David J. Thomas, thePortus.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE.
```
