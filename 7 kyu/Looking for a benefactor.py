import math
def new_avg(arr, newavg):
    value = math.ceil(newavg * (len(arr) + 1) - sum(arr))
    if value > 0:
        return value
    else:
        raise ValueError