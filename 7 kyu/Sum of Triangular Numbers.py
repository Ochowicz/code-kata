def sum_triangular_numbers(n):    
    return sum((1+n)/2*n for n in range(1, n+1)) if n > 0 else 0