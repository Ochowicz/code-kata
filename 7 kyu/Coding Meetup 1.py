def count_developers(lst):
    return sum(obj['language'] == 'JavaScript' and  obj['continent'] == 'Europe' for obj in lst)