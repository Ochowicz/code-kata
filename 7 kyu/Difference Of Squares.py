def difference_of_squares(n):
    if 1<= n <= 100:
        return (sum(i for i in range(n + 1))) ** 2 - sum(i ** 2 for i in range(n + 1))