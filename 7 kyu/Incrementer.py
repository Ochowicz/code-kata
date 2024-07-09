def incrementer(nums):
    return [(i + j + 1) % 10 for i, j in enumerate(nums)]