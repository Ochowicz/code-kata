def contain_all_rots(strng, arr):
    if not strng:
        return True

    def get_rotations(s):
        return [s[i:] + s[:i] for i in range(len(s))]

    rotations = get_rotations(strng)

    for rotation in rotations:
        if rotation not in arr:
            return False

    return True