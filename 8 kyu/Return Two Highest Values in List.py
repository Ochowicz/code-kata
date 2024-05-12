# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.
#
# The result should also be ordered from highest to lowest.
#
# Examples:
#
# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []
def two_highest(arg1):
    unique_elements = list(set(arg1))
    if len(unique_elements) <= 1:
        return unique_elements
    else:
        sorted_unique = sorted(unique_elements, reverse=True)
        if len(sorted_unique) >= 2 and sorted_unique[0] == sorted_unique[1]:
            return [sorted_unique[0]] + sorted_unique[2:]
        else:
            return sorted_unique[:2]