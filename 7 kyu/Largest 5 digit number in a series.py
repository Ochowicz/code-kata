def solution(digits):
    return max(int(digits[n:n+5]) for n in range(len(digits)))