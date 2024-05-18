def animals(heads, legs):
    if heads < 0 or legs < 0:
        return 'No solutions'
    elif heads == 0 and legs == 0:
        return (0, 0)
    else:
        chickens = (4 * heads - legs) / 2
        cows = heads - chickens
        if chickens >= 0 and cows >= 0 and chickens % 1 == 0 and cows % 1 == 0:
            return (chickens, cows)
        else:
            return 'No solutions'
