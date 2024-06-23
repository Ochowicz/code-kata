def solve(arr): 
    result = []
    for num in reversed(arr):
        if num not in result:
            result.append(num)
    return result[::-1]