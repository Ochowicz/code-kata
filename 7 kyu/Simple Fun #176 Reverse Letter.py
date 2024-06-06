def reverse_letter(st):
    return ''.join(char for char in st[::-1] if char.isalpha())