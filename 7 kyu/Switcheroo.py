def switcheroo(s):
    dict = {
        'a': 'b',
        'b': 'a',
        'c': 'c'
              }
    return ''.join(dict[i] for i in s)