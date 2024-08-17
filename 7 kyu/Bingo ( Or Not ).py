def bingo(array):
    return 'WIN' if {ord(i) - 64 for i in 'BINGO'}.issubset(set(array)) else 'LOSE'