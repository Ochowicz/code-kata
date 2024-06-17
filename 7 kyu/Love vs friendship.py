def words_to_marks(s):
    return sum(ord(x) - ord('a') + 1 for x in s)