def triple_trouble(one, two, three):
    grouped_letters = ''
    for i in range(len(one)):
        grouped_letters += one[i] + two[i] + three[i]
    return grouped_letters