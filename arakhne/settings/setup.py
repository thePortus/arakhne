
# Currently Supported Languages
SUPPORTED_LANGS = [None, 'english', 'latin', 'greek']

# Required systems for the NLTK and CLTK
SUPPORTED_SYSTEMS = {
    'base': ['posix', 'nt', 'ce', 'java'],
    'nltk': ['posix'],
    'cltk': ['posix']
}

# Languages powered by the NLTK
NLTK_LANGS = ['english']

# Languages powered by the CLTK
CLTK_LANGS = ['latin', 'greek']


# Necessary Python Modules for each Toolkit
MODULES = {
    'nltk': ['nltk'],
    'cltk': ['nltk', 'cltk'],
}

PACKAGES = {
    # Natural Language Toolkit Language Requirements
    # NLTK requirements come in tuple form, (package_name, data_path)
    'nltk': {
        'all': [
            (
                'verbnet',
                'corpora/verbnet'
            ), (
                'wordnet',
                'corpora/wordnet'
            ), (
                'words',
                'corpora/words'
            ), (
                'large_grammars',
                'grammars/large_grammars'
            ), (
                'averaged_perceptron_tagger',
                'taggers/averaged_perceptron_tagger'
            ), (
                'hmm_treebank_pos_tagger',
                'taggers/hmm_treebank_pos_tagger'
            ), (
                'maxent_treebank_pos_tagger',
                'taggers/maxent_treebank_pos_tagger'
            ), (
                'universal_tagset',
                'taggers/universal_tagset'
            ), (
                'punkt',
                'tokenizers/punkt'
            ), (
                'maxent_ne_chunker',
                'chunkers/maxent_ne_chunker'
            ),
        ],
        # English Packages
        'english': [
            (
                'stopwords',
                'corpora/stopwords'
            ),
        ]
    },
    # Classical Language Toolkit Language Requirements
    'cltk': {
        # Latin Packages
        'latin': [
            'latin_text_perseus',
            'latin_treebank_perseus',
            'latin_treebank_perseus',
            'latin_text_latin_library',
            'latin_proper_names_cltk',
            'latin_models_cltk',
            'latin_pos_lemmata_cltk',
            'latin_treebank_index_thomisticus',
            'latin_lexica_perseus',
            'latin_training_set_sentence_cltk',
            'latin_word2vec_cltk',
            'latin_text_antique_digiliblt',
            'latin_text_corpus_grammaticorum_latinorum'
        ],
        # Greek Packages
        'greek': [
            'greek_software_tlgu',
            'greek_text_perseus',
            'greek_proper_names_cltk',
            'greek_models_cltk',
            'greek_treebank_perseus',
            'greek_lexica_perseus',
            'greek_training_set_sentence_cltk',
            'greek_word2vec_cltk',
            'greek_text_lacus_curtius'
        ]
    }
}

OBSOLETE_CLTK_PACKAGES = ['phi5', 'phi7', 'tlg']
