def split_the_bill(x):
    total = sum(x.values())
    average = total / len(x)

    result = {}
    for person, spent in x.items():
        result[person] = round(x[person] - average, 2)

    return result