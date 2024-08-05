from preloaded import animals, elements


def chinese_zodiac(year):
    return f'{elements[((year - 1924) // 2) % 5]} {animals[(year - 1924) % 12]}'