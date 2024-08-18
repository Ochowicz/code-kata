def reverse_bits(n):
    return int(str(bin(n)[2:])[::-1], 2)