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

# All corpora
CORPORA_ALL = {
    'meta_fields': [],
    'text_col': None
}

STOPWORDS = {
    'base': 'defaults/base.txt',
    'english': 'defaults/english.txt',
    'greek': 'defaults/greek.txt',
    'latin': 'defaults/latin.txt'
}
