def partlist(arr):
    return [(' '.join(arr[:n]), ' '.join(arr[n:])) for n in range(1, len(arr))]