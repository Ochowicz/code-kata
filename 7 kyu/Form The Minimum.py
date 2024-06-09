def min_value(digits):
    return int(''.join(map(str, sorted(list(dict.fromkeys(digits))))))