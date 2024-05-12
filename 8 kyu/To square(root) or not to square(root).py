# Write a method, that will get an integer array as parameter and will process every number from this array.
#
# Return a new array with processing every number of the input-array like this:
#
# If the number has an integer square root, take this, otherwise square the number.
from math import sqrt
def square_or_square_root(arr):
    return [sqrt(x) if int(sqrt(x)) == sqrt(x) else x**2 for x in arr]