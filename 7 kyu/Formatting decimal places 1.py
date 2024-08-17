def two_decimal_places(number):
    for i, v in enumerate(str(number)):
        if v is '.':
            return float(str(number)[:i+3])