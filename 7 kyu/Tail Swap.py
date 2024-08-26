def tail_swap(strings):
    a, b = strings
    a1, a2 = a.split(':')
    b1, b2 = b.split(':')
    return [':'.join([a1, b2]), ':'.join([b1, a2])]