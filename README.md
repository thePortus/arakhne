# Arakhne Text Loom:

<small>Corpus Analytics for English, Latin, and Greek</small>

*By David J. Thomas, [thePortus.com](http://theportus.com/)*

---

![Travis CI Badge](https://travis-ci.org/thePortus/arakhne.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/thePortus/arakhne/badge.svg?branch=master)](https://coveralls.io/github/thePortus/arakhne?branch=master)

---

Scrub and analyze CSVs or folders of English, Latin and Greek text data, working with corpora just like a list of documents!

Powered by the [NLTK](http://www.nltk.org/) and [CLTK](https://github.com/cltk/cltk) modules, Arakhne attemps to make the scrubbing and analysis of mass volumes of texts accessible to the Ancient Scholar with minimal Python training. The goal of Arakhne is to allow the user to perform the greatest number of changes in the fewest number of commands possible, all while maintaining semantic clarity.

My students have great analytical questions, but limited programming experience. They needed to get on with the business of scholarly analysis. So, I created Arakhne so that they could load, scrub, analyze, and save a large corpus of texts in a few short lines of code. Since then, it has gr

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
"1","Card 1","This is just some sample 
text",
"2","Card 2","because lorem ipsum won't work well for english examples."
"3","Card 3","... so please bare[sic] with this b-
oring set!"
```


# Loading

Importing Arakhne
``` python
>>> from arakhne import Arakhne
```

Setting language and loading a CSV
``` python
>>> from arakhne import Arakhne
>>> sample = Arakhne().corpus('english').csv().load('sample.csv')
Loading /Users/davidthomas/Git/arakhne/sample.csv
Corpus loaded successfully.
```

Specifying custom settings by passing a dictionary to the csv method
``` python
>>> from arakhne import Arakhne
>>> settings={ 'text_col': 'Report' }
>>> sample = Arakhne().corpus('english').csv(settings).load('sample.csv')
```

# Accessing Data

Looping through text documents
``` python

# Arakhne treats your documents and corpora just like a normal Python list
print(sample)
['This is just some sample \ntext', "because lorem ipsum won't work well for english examples.", '...    so please bare[sic] with this b-\noring set!']
# Access individual elements or splices
print(sample[0])
'This is just some sample \ntext'
# Access document information through the .metadata property
print(sample[0].metadata)
{"id": "1", "title": "Card 1"}
```

# Saving
Saving corpus data (only CSVs at the moment)
``` python
>>> sample.csv().save('sample_scrubbed.csv')
Corpus saved sucessfully.
```
Overwriting an existing file
``` python
>>> sample.csv(settings={'overwrite': True}).save('sample.csv')
```

---

## Downloading NLTK/CLTK Requirements (OSX/Linux Only)

Use Arakhne to downlown necessary Python modules and NLTK/CLTK trainer packages
``` python
# Download all requirements
>>> Arakhne().corpus('english').get.all()
# Download just the pip module(s)
>>> Arakhne().corpus('english').get.modules()
# Download only the relevant NLTK/CLTK corpora/trainer sets
>>> Arakhne().corpus('english').get.packages()
```

---

## Text Tools All Languages

Remove endline chars, collapsing each text to a single line
``` python
>>> scrubbed_corpus = sample.rm_lines()
['This is just some sample  text', "because lorem ipsum won't work well for english examples.", '...    so please bare[sic] with this boring set!']
```
Delete editorial statements (i.e. text inside ()[]{}<>, etc).
``` python
>>> scrubbed_corpus = sample.rm_edits()
['This is just some sample \ntext', "because lorem ipsum won't work well for english examples.", '...    so please bare with this b-\noring set!']
```
Filter non-language specific alphabetic characters
``` python
>>> scrubbed_corpus = sample.rm_nonchars()
['This is just some sample text', 'because lorem ipsum wont work well for english examples', '    so please baresic with this boring set']s
```
Collapse blocks of redundant whitespace and trim leading/trailing spaces
``` python
>>> scrubbed_corpus = sample.rm_spaces()
['This is just some sample text', "because lorem ipsum won't work well for english examples.", '... so please bare[sic] with this b- oring set!']
```
Filter out docs not containing a Regex search pattern
``` python
>>> filtered_corpus = sample.re_search('lorem ipsum')
["because lorem ipsum won't work well for english examples.",]
```
Methods can be chained to perform multi-operation statements
``` python
>>>sample = sample.rm_lines().rm_edits().rm_nonchars().rm_spaces()
['This is just some sample text', 'because lorem ipsum wont work well for english examples', 'so please bare with this boring set']
```

## Text Tools Greek

For the following examples, one sample document is given
``` python
'[2]\n       ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ, πρότερον δὲ πρὶν ἢ Θεμιστοκλῆς Ἀθηναίοις ἦρξεν ἐπίνειον οὐκ ἦν: Φαληρὸν δέ—ταύτῃ γὰρ ἐλάχιστον ἀπέχει τῆς πόλεως ἡ θάλασσα—'
```

Normalize Greek accent issues, otherwise leaving text unchanged
``` python
>>> sample = sample.normalize()
'[2]\n       ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ, πρότερον δὲ πρὶν ἢ Θεμιστοκλῆς Ἀθηναίοις ἦρξεν ἐπίνειον οὐκ ἦν: Φαληρὸν δέ—ταύτῃ γὰρ ἐλάχιστον ἀπέχει τῆς πόλεως ἡ θάλασσα—'
```
CLTK's TLGU Cleanup auto-scrubs Greek text for analysis
``` python
>>> sample = sample.tlgu_clean_up()
' ὁ δὲ Πειραιεὺς δῆμος μὲν ἦν ἐκ παλαιοῦ πρότερον δὲ πρὶν ἢ Θεμιστοκλῆς Ἀθηναίοις ἦρξεν ἐπίνειον οὐκ ἦν Φαληρὸν δέ—ταύτῃ γὰρ ἐλάχιστον ἀπέχει τῆς πόλεως ἡ θάλασσα—'
```
Lemmatize each text, making it easier to search TAKES A LONG TIME
``` python
sample = sample.lemmatize()
['[ 2 ] ὁ δὲ πειραιεὺς δῆμος μὲν εἰμί ἐκ παλαιόω , πρότερος δὲ πρὶν ἢ θεμιστοκλέης ἀθηναῖος ἄρχω ἐπίνειον οὐ εἰμί : φαληρὸν δέ—ταύτῃ γὰρ ἐλάχιστος ἀπέχω ὁ πόλις ὁ θάλασσα—']
```

OTHER AVAILABLE TOOLS (TO BE EXPANDED AND IMPROVED)
``` python
# Meter Scansion
>>> scanned_lines = sample.scansion()
# Named entity recognition
>>> entity_list = sample.entities()
# Part of speech tagging
>>> parsed_words = sample.tag()
```

## Text Tools Latin

``` python
# Alternative to lemmatize, reduce words to stems
>>> sample = sample.stemmify()
# Normalize swaps i's in for j's and u's in for v's
>>> sample = sample.normalize()
# Macronize adds macrons to long vowels
>>> sample = sample.macronize()
# Meter Scansion
>>> scanned_lines = sample.scansion()
# Further poetic tool on top of scansion, clausulae analysis
>>> clausulae = sample.clausulae()
# Named entity recognition
>>> entity_list = sample.entities()
# Part of speech tagging
>>> parsed_words = sample.tag()
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
