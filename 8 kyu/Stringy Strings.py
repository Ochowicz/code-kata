def stringy(size):
    if size % 2 == 0:
        return '10' * (size // 2)
    else:
        return '1' + '01' * (size // 2)