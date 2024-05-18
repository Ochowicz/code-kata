def is_opposite(s1,s2):
    if s1.lower() == s2.lower():
        for i, j in zip(s1, s2):
            if i != j:
                return True
            else:
                return False
    return False