def count_squares(cuts):
    if cuts == 0:
        return 1
    else:
        return (cuts + 1) ** 3 - (cuts - 1) ** 3