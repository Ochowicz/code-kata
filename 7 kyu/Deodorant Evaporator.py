def evaporator(content, evap_per_day, threshold):
    days = 0
    n = 100
    while n > threshold:
        days += 1
        n *= (100 - evap_per_day) / 100
    return days