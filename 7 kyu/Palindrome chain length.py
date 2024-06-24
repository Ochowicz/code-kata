def palindrome_chain_length(n):
    step = 0
    while step < 100 and n != int(str(n)[::-1]):
        n += int(str(n)[::-1])
        step += 1
    return step