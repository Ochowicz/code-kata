def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def subtract_sum(number):
    fruits = [
        "kiwi", "pear", "kiwi", "banana", "melon", "banana", "melon", "pineapple",
        "apple", "pineapple", "cucumber", "pineapple", "cucumber", "orange", "grape",
        "orange", "grape", "apple", "grape", "cherry", "pear", "cherry", "pear",
        "kiwi", "banana", "kiwi", "apple", "melon", "banana", "melon", "pineapple",
        "melon", "pineapple", "cucumber", "orange", "apple", "orange", "grape",
        "orange", "grape", "cherry", "pear", "cherry", "pear", "apple", "pear",
        "kiwi", "banana", "kiwi", "banana", "melon", "pineapple", "melon", "apple",
        "cucumber", "pineapple", "cucumber", "orange", "cucumber", "orange", "grape",
        "cherry", "apple", "cherry", "pear", "cherry", "pear", "kiwi", "pear",
        "kiwi", "banana", "apple", "banana", "melon", "pineapple", "melon",
        "pineapple", "cucumber", "pineapple", "cucumber", "apple", "grape",
        "orange", "grape", "cherry", "grape", "cherry", "pear", "cherry", "apple",
        "kiwi", "banana", "kiwi", "banana", "melon", "banana", "melon", "pineapple",
        "apple", "pineapple"
    ]

    while number >= 10 and number <= 10000:
        sum_digits = sum_of_digits(number)
        number = number - sum_digits

        if number <= 100 and number >= 1:
            return fruits[number - 1]