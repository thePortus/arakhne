# Arakhne Text Loom:

<small> Greek and Latin Text Analysis/Scrubbing Optimized for Corpora </small>

*By David J. Thomas, [thePortus.com](http://theportus.com/)*

---

![Travis CI Badge](https://travis-ci.org/thePortus/arakhne.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/thePortus/arakhne/badge.svg?branch=master)](https://coveralls.io/github/thePortus/arakhne?branch=master)

---

Scrub and analyze entire files of Greek and Latin text data, working with the corpus just like a list of documents.

Powered by the [NLTK](http://www.nltk.org/) and [CLTK](https://github.com/cltk/cltk) modules, Arakhne attemps to make the scrubbing and analysis of mass volumes of texts accessible to the Ancient Scholar with minimal Python training. The goal of Arakhne is to allow the user to perform the greatest number of changes in the fewest number of commands possible, all while maintaining semantic clarity.

I created Arakhne Text Loom so that my students, who have limited programming experience, could load, scrub, analyze, and save a large corpus of texts in a few short lines of code.

The [Natural Language Toolkit](https://nltk.org) has enabled modern text analysis for some years now. Recently, the amazing [Classical Language Toolkit, or CLTK](http://cltk.org), has brought machine language processing to ancient studies. The CLTK library powers the majority of operations behind this module. However, CLTK operations focus on analyzing single bits of text (or other data focused on a single 'document').

As Latinists well know, a *textus* is literally 'something woven.' With Arakhne, you can unravel a corpus and explore the documents, words, people, and places that bind the documents together.

---

## Contents
* [Installation](#installation)
* [Sample Data](#sample-data)
* [Loading](#loading)
* [Accessing Data](#accessing-data)
* [Saving](#saving)
* [Downloading Trainer Corpora](#downloading-trainer-corpora)
* [Text Tools: All Languages](#text-tools-all-languages)
* [Text Tools: Greek](#text-tools-greek)
* [Text Tools: Latin](#text-tools-latin)
* [License](#license)

---

## Installation

``` python
pip install arakhne
```

---

## Sample Data

Below is the sample raw corpus, used in the following examples.
``` bash
# ========sample.csv ========
"id","title","text"
"1","Card 1","αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος  Κελεοῖο,\n\n185 βὰν",
"2","Card 2","200ἀλλ᾽ ἀγέλαστος,  ἄπαστυς[ος] ἐδητύος ἠδὲ ποτῆτος"
"3","Card 3","... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```


# Loading

Importing Arakhne
``` python
>>> from arakhne import Arakhne
```

Setting language and loading a CSV
``` python
>>> sample = Arakhne('greek').corpus.load.csv('sample.csv')
Loading /path/to/sample.csv
Corpus loaded successfully.
```

Specifying a custom column containing text data
``` python
>>> sample = Arakhne('greek').corpus.load.csv('sample.csv', text_col='a_col')
```

# Accessing Data

Looping through text documents
``` python
>>> for doc in sample:
>>>     print(doc)
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος  Κελεοῖο,\n\n185 βὰν"
"200ἀλλ᾽ ἀγέλαστος,  ἄπαστυς[ος] ἐδητύος ἠδὲ ποτῆτος"
"... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```
Accessing document metadata
``` python
>>> for doc in sample:
>>>     print(doc.metadata)
{"id": "1", "title": "Card 1"}
{"id": "2", "title": "Card 2"}
{"id": "3", "title": "Card 3"}
```

# Saving
Saving corpus data (only CSVs at the moment)
``` python
>>> sample.save.csv('sample_scrubbed.csv')
Corpus saved sucessfully.
```
Overwriting an existing file
``` python
>>> sample.save.csv('sample.csv', overwrite=True)
Corpus saved sucessfully.
```

---

## Downloading Trainer Corpora

Use Arakhne to do a one-time download of NLTK & CLTK trainer sets
``` python
>>> Arakhne('english').downloader.nltk()
>>> Arakhne('greek').downloader.cltk()
>>> Arakhne('latin').downloader.cltk()
```

---

## Text Tools All Languages

Remove endline chars, collapsing each text to a single line
``` python
>>> sample = sample.rm_lines()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος  Κελεοῖο,  185 βὰν"
"200ἀλλ᾽ ἀγέλαστος,  ἄπαστυς[ος] ἐδητύος ἠδὲ ποτῆτος"
"... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```
Delete editorial statements (i.e. text inside ()[]{}<>, etc).
``` python
>>> sample = sample.rm_edits()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος  Κελεοῖο,\n\n185 βὰν"
"200ἀλλ᾽ ἀγέλαστος,  ἄπαστυς ἐδητύος ἠδὲ ποτῆτος"
"... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```
Filter non-language specific alphabetic characters
``` python
>>> sample = sample.rm_nonchars()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος  Κελεοῖο, βὰν"
"ἀλλ᾽ ἀγέλαστος,  ἄπαστυςος ἐδητύος ἠδὲ ποτῆτος"
" τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα"
```
Collapse blocks of redundant whitespace and trim leading/trailing spaces
``` python
>>> sample = sample.rm_spaces()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος Κελεοῖο,\n\n185 βὰν"
"200ἀλλ᾽ ἀγέλαστος, ἄπαστυς[ος] ἐδητύος ἠδὲ ποτῆτος"
"... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```
Filter out docs not containing a Regex search pattern
``` python
>>> sample = sample.re_search('μύθων')
"... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```
Methods can be chained to perform multi-operation statements
``` python
>>>sample = sample.rm_lines().rm_edits().rm_nonchars().rm_spaces()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος Κελεοῖο, βὰν"
"ἀλλ᾽ ἀγέλαστος, ἄπαστυς ἐδητύος ἠδὲ ποτῆτος"
"τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα"
```

## Text Tools Greek

Normalize Greek accent issues, otherwise leaving text unchanged
``` python
>>> sample = sample.normalize()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος  Κελεοῖο,  185 βὰν"
"200ἀλλ᾽ ἀγέλαστος,  ἄπαστυς[ος] ἐδητύος ἠδὲ ποτῆτος"
"... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```
CLTK's TLGU Cleanup auto-scrubs Greek text for analysis
``` python
>>> sample = sample.tlgu_clean_up()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος Κελεοῖο, βὰν"
"ἀλλ᾽ ἀγέλαστος, ἄπαστυς ἐδητύος ἠδὲ ποτῆτος"
"τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα"
```
Lemmatize each text, making it easier to search TAKES A LONG TIME
``` python
sample = sample.lemmatize()
"αἶψα δὲ δώμαθ᾽ ἵκοντο διοτρεφέος  Κελεοῖο,  185 βὰν"
"200ἀλλ᾽ ἀγέλαστος,  ἄπαστυς[ος] ἐδητύος ἠδὲ ποτῆτος"
"... τῇσι δὲ μύθων ἦρχεν ἐύζωνος Μετάνειρα:"
```
Perform scansion, returning lists of lines containing beat information
``` python
>>> scanned_lines = sample.scansion()
```
Generate a list of lists of strings with entities (TO BE EXPANDED)
``` python
>>> entity_list = sample.entities()
```
Returns a list of lists of tuple pairs of the word/part of speech
``` python
>>> parsed_words = sample.tag()
```

## Text Tools Latin

Macronize adds macrons to long vowels
``` python
>>> sample = sample.macronize()
```
Normalize swaps i's in for j's and u's in for v's
``` python
>>> sample = sample.normalize()
```
Further poetic tool on top of scansion, clausulae analysis
``` python
>>> clausulae = sample.clausulae()
```
Stemmify is alternative to lemmatization, reducing words to stems
``` python
>>> sample = sample.stemmify()
```

---

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
