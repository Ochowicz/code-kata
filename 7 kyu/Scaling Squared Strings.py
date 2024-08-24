def scale(strng, k, v):
    if not strng:
        return ""
    horizontally_scaled = [''.join(char * k for char in line) for line in strng.splitlines()]
    vertically_scaled = [line for line in horizontally_scaled for _ in range(v)]
    return '\n'.join(vertically_scaled)
12 hours agoRefactorDiscuss