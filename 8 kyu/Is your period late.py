def period_is_late(last, today, cycle_length):
    difference = (today - last).days
    return difference > cycle_length