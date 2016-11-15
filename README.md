# Arakhne Text Loom:

<small> Greek and Latin Text Analysis/Scrubbing Optimized for Corpora </small>

*By David J. Thomas, [thePortus.com](http://theportus.com/)*

---

![Travis CI Badge](https://travis-ci.org/thePortus/arakhne.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/thePortus/arakhne/badge.svg?branch=master)](https://coveralls.io/github/thePortus/arakhne?branch=master)

---

Powered by the [NLTK](http://www.nltk.org/) and [CLTK](https://github.com/cltk/cltk) modules, Arakhne attemps to make the scrubbing and analysis of mass volumes of texts accessible to the Ancient Scholar with minimal Python training. The goal of Arakhne is to allow the user to perform the greatest number of changes in the fewest number of commands possible, all while maintaining semantic clarity.

I created Arakhne Text Loom so that my students, who have limited programming experience, could load, scrub, analyze, and save a large corpus of texts in a few short lines of code.

The [Natural Language Toolkit](https://nltk.org) has enabled modern text analysis for some years now. Recently, the amazing [Classical Language Toolkit, or CLTK](http://cltk.org), has brought machine language processing to ancient studies. The CLTK library powers the majority of operations behind this module. However, CLTK operations focus on analyzing single bits of text (or other data focused on a single 'document').

As Latinists well know, a *textus* is literally 'something woven.' By unraveling a corpus into a series of documents, words, entities, and the threads that bind them together.

---

## Contents
* [Installation](#installation)
* [Basic Use](#basic-use)
* [Downloading Corpora](#downloading-corpora)
* [Text-Scrubbing](#text-scrubbing)
* [Textual Analytics](#textual-analytics)
* [License](#license)

---

## Installation

``` python
pip install arakhne
```

---

## Basic Use

``` python
from arakhne import Arakhne

# Load .csv file containing as an Arakhne corpus object
sample = Arakhne('latin').corpus.load.csv('path/to/sample.csv')

# Perform some operation and store the resulting corpus
sample = sample.some_scrubbing_method()

# Export the results to a .csv
sample.save.csv('path/to/save.csv')
```

---

## Downloading Corpora
``` python

# Use Arakhne to launch the NLTK downloader to get trainer sets
Arakhne('english').downloader.nltk()

# Use Arakhne to download all of the CLTK corpora for a language
Arakhne('greek').downloader.cltk()
Arakhne('latin').downloader.cltk()

```
---

## Text Scrubbing

*Further tools and methods to be added*
``` python
# ==============
# ALL LANGUAGES
# ==============
# Remove endline chars and collapse each text to a single line
sample = sample.rm_lines()
# Delete editorial statements (i.e. text inside ()[]{}<>, etc).
sample = sample.rm_edits()
# Filter non-language specific alphabetic characters
sample = sample.rm_nonchar()
# Collapse blocks of redundant whitespace into a single space
sample = sample.rm_spaces()
# Methods can be chained to perform multi-operation statements
sample = sample.rm_lines().rm_edits().rm_nonchar().rm_spaces()

# ==============
# GREEK-ONLY
# ==============
# Normalize smoothes over some Greek accent encoding issues
sample = sample.normalize()
# CLTK's TLGU Cleanup auto-scrubs Greek text for analysis
sample = sample.tlgu_clean_up()

# ==============
# Latin-ONLY
# ==============
# Macronize adds macrons to long vowels
sample = sample.macronize()
# Normalize swaps i's in for j's and u's in for v's
sample = sample.normalize()
```

---

## Textual Analytics

*Further tools and methods to be added*
``` python
# ==============
# ALL LANGUAGES
# ==============
# Returns new corpus with only matching docs. Can take Regex expressions
filtered_sample = sample.re_search('sample search pattern')

# ==============
# GREEK OR LATIN
# ==============
# Lemmatize each text, making it easier to search TAKES A LONG TIME
sample = sample.lemmatize()
# Performs scansion, returning lists of lines containing beat information
scanned_lines = sample.scansion()
# Generates a list of lists of strings with entities (TO BE EXPANDED)
entity_list = sample.entities()

# ==============
# GREEK-ONLY
# ==============
# Returns a list of lists of tuple pairs of the word/part of speech
parsed_words = sample.tag()

# ==============
# Latin-ONLY
# ==============
# Further poetic tool on top of scansion, clausulae analysis
clausulae = sample.clausulae()
# Stemmify is alternative to lemmatization, reducing words to stems
sample = sample.stemmify()
```

*Further tools and methods to be added*

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
