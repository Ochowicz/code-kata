def row_sum_odd_numbers(n):
    return sum([1+2*x for x in range(sum(range(n)), sum(range(n+1)))])