import math


def square_area(A):
    # Obliczanie promienia na podstawie długości łuku
    r = 2 * A / math.pi
    # Obliczanie pola kwadratu
    pole = round(r ** 2, 2)

    return pole