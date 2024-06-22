def solve(strings : list[str]) -> list[int]:
    return [sum((ord(char.lower())-ord('a')) == i for i, char in enumerate(string)) for string in strings]