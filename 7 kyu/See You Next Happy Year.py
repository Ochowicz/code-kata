
def next_happy_year(year):
    new = year + 1
    while sum(str(new).count(i) for i in str(new)) != 4:
        new += 1
    return new