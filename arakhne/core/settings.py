
""" =========== LANGUAGES =========== """

# Valid languages
SUPPORTED_LANGS = [None, 'english', 'latin', 'greek']


""" =========== FILES =========== """

# All files
FILES_ALL = {
    'path_type': 'relative',
    'newline': '',
    'encoding': 'utf-8',
    'overwrite': True,
}

# CSV files
FILES_CSV = FILES_ALL
FILES_CSV.update({
    'delimiter': ',',
    'quotechar': '"',
    'dialect': 'excel',
    'text_col': 'text',
})


""" =========== CORPORA =========== """

# All corpora
CORPORA_ALL = {
    'meta_fields': [],
    'text_col': None
}
