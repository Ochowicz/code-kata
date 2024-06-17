def even_numbers(arr,n):
    return list(filter(lambda i: i % 2 == 0, arr))[-n:]