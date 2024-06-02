def high_and_low(numbers):
    numbers = numbers.split(' ')
    lst = []
    for number in numbers:
        lst.append(int(number))
    return f"{max(lst)} {min(lst)}"