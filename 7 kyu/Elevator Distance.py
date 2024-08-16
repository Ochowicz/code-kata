def elevator_distance(array):
    return sum(abs(i - j) for i, j in zip(array, array[1:]))