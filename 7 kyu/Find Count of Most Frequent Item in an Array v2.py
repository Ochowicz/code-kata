def most_frequent_item_count(collection):
    dic = {}
    for i in collection:
        dic.setdefault(i, 0)
        dic[i] += 1
    return max(dic.values()) if dic else 0