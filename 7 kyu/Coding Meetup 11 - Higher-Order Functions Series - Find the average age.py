def get_average(lst):
    return round(sum(i['age'] for i in lst)/len(lst)) if lst else None