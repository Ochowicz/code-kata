def check_three_and_two(array):
    count = [array.count(string) for string in array]
    return 3 in count and 2 in count