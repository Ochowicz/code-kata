def smaller(arr):
    return [sum(arr[j] < arr[i] for j in range(i + 1, len(arr))) for i in range(len(arr))]