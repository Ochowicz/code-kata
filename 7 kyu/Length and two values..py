def alternate(n, first_value, second_value):
    return [(first_value, second_value)[i%2] for i in range(n)]