def sort_my_string(s):
    even = ''.join(letter for i, letter in enumerate(s) if i % 2 == 0)
    odd = ''.join(letter for i, letter in enumerate(s) if i % 2 != 0)
    return f'{even} {odd}'