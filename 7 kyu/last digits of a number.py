def solution(n,d):
    return list(map(int, str(n)))[-d:] if d > 0 else []