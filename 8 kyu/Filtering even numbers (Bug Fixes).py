def kata_13_december(lst):
    solution = []
    for i in range(len(lst)):
        if lst[i]%2!=0:
            solution.append(lst[i])
    return solution