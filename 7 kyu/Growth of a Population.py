def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = (p0 * (1 + percent / 100) + aug) // 1
        years += 1
    return years