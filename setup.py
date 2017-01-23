try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': "arakhne",
    'packages': [
        "arakhne",
        "arakhne.common",
        "arakhne.corpus",
        "arakhne.corpus.files",
        "arakhne.doc",
        "arakhne.settings",
        "arakhne.setup",
        "arakhne.stopwords"
    ],
    'install_requires': ["nltk", "cltk"],
    'version': "0.3.1",
    'description': "Arakhne Classical Text Loom for Corpus-Based Analytics",
    'author': "David J. Thomas",
    'author_email': "dave.a.base@gmail.com",
    'url': "https://github.com/thePortus/arakhne",
    'download_url': "https://github.com/thePortus/arakhne/archive/master.zip",
    'keywords': [
        "nlp",
        "nltk",
        "cltk",
    ],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Sociology :: History"
    ],
}

setup(**config)
