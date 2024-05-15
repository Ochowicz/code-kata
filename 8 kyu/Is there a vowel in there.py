def is_vow(inp):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(inp)):
        if chr(inp[i]) in vowels:
            inp[i] = chr(inp[i])
    return inp