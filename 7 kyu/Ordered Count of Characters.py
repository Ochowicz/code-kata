def ordered_count(inp):
    dictionary = {}
    order = []
    for letter in inp:
        if letter not in dictionary:
            dictionary[letter] = 1
            order.append(letter)
        else:
            dictionary[letter] += 1
    return [(letter, dictionary[letter]) for letter in order]