try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': "arakhne",
    'packages': [
        "arakhne",
        "arakhne.core",
        "arakhne.corpus",
        "arakhne.doc",
        "arakhne.fixtures",
        "arakhne.get",
        "arakhne.tests"
    ],
    'install_requires': ["nltk", "cltk"],
    'version': "0.2.3",
    'description': "Arakhne Text Loom for Corpus-Based Classical-Language Analytics",
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
