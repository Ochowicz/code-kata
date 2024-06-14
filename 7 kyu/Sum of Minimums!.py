def sum_of_minimums(numbers):
    return sum(map(min, (row for row in numbers)))