dic = {
    ('R', 'R'): 'R',
    ('B', 'B'): 'B',
    ('G', 'G'): 'G',
    ('R', 'G'): 'B',
    ('G', 'R'): 'B',
    ('R', 'B'): 'G',
    ('B', 'R'): 'G',
    ('G', 'B'): 'R',
    ('B', 'G'): 'R',
}

def triangle(row):
    while len(row) > 1:
        row = ''.join(dic[(i, j)] for i, j in zip(row, row[1:]))
    return row