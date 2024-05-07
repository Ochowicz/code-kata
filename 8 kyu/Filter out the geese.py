geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    result = []
    for elem in birds:
        if elem not in geese:
            result.append(elem)
    return result