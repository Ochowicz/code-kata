def name_value(my_list):
    return [sum(ord(char) - 96 for char in string if char != ' ') * (index + 1) for index, string in enumerate(my_list)]