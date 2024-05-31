def next_item(xs, item):
    iterator = iter(xs)
    for current in iterator:
        if current == item:
            return next(iterator, None)
    return None