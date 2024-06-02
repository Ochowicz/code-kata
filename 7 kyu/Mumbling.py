def accum(st):
    result = []
    for index, char in enumerate(st):
        result.append(f'{char.upper()}{char.lower()*(index)}')
    return '-'.join(result)