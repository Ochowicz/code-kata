def divisors(n):
    return sum(n % x == 0 for x in range(1, n + 1))
