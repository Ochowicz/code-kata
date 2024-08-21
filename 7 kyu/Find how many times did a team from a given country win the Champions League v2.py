def count_wins(winners_list, country):
    return sum(1 for winner in winners_list if winner['country'] == country)