# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.
def between(a,b):
    return [n for n in range(a, b + 1)]