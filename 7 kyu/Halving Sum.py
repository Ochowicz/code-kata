def halving_sum(n): 
    total_sum = 0
    while n > 0:
        total_sum += n
        n //= 2
    return total_sum