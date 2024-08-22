def next_happy_year(year):
    new = year + 1
    while len(set(str(new))) != 4:
        new += 1
    return new