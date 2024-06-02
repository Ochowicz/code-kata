def open_or_senior(data):
    return ['Senior' if krotka[0] >= 55 and krotka[1] > 7 else 'Open' for krotka in data]