def paint_letterboxes(start, finish):
    numbers = ''.join(list(map(str, [x for x in range(start, finish + 1)])))
    return [numbers.count(str(i)) for i in range(10)]