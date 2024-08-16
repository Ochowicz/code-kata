def minimum_steps(numbers, value):
    result = 0
    step = -1
    numbers.sort(reverse=True)
    while result < value:
        result += numbers.pop()
        step += 1
    return step
