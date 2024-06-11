import re
def sum_of_a_beach(beach):
    return len(re.findall(r'sand|water|fish|sun', beach, re.I))