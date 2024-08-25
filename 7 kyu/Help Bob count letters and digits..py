def count_letters_and_digits(s):
    return sum(i.isalnum() for i in s)