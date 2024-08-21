def count_wins(winners_list, country):
    count = 0
    for line in winners_list:
        if line['country'] == country:
            count += 1
    return count