def find_deleted_number(arr, mixed_arr):
    try:
        return (set(arr) - set(mixed_arr)).pop()
    except:
        return 0