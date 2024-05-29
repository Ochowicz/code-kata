def add_length(str_):
    words = str_.split(' ')
    return [f'{word} {len(word)}' for word in str_.split(' ')]