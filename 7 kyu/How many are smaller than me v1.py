def smaller(arr):
    result = []
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                count += 1
        result.append(count)
    return result