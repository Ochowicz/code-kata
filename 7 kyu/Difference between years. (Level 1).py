import re
def how_many_years (date1,date2):
    date1 = int(re.search(r'^\d+', date1)[0])
    date2 = int(re.findall(r'^\d+', date2)[0])
    return abs(date1 - date2)