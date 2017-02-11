"""Arakhne

===============================================================================
============================== Arakhne Text Loom ==============================
===============================================================================

Arakhne makes the scrubbing and analysis of mass volumes of texts accessible to
the Ancient Scholar with minimal Python training. The goal of Arakhne is to
allow the user to perform the greatest number of changes in the fewest number
of commands possible, all while maintaining semantic clarity.

For more information, see
https://github.com/thePortus/arakhne

"""

import sys
from pkg_resources import get_distribution

from .setup import Setup
from .corpus import Corpus

if sys.version_info[0] != 3:
    raise ImportError('Python Version 3 or above is required for cltk.')

__author__ = 'David J. Thomas'

__copyright__ = 'Copyright (c) 2016 David J. Thomas. Distributed and Licensed under the MIT License.'

__description__ = __doc__

__license__ = 'MIT'

__url__ = 'http://github.com/thePortus/arakhne'

__version__ = get_distribution('arakhne').version


def Arakhne(language=None):
    # if not Setup(language=language).setup():
    #     raise Exception('Problem encountered during setup.')
    # Return an empty corpus of appropriate language
    return Corpus(language).make()


# Cleaning up namespaces
del get_distribution
del sys
