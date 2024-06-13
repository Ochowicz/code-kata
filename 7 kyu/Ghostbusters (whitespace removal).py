import re
def ghostbusters(building):
    whitespace = re.compile(r'\s+')
    return whitespace.sub('', building) if whitespace.search(building) else "You just wanted my autograph didn't you?"