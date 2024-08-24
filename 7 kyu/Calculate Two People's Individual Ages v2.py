def get_ages(sum_, difference):
    older = (sum_ + difference) / 2
    younger = older - difference
    if older >= 0 and younger >= 0 and sum_ >= 0 and difference >= 0:
        return (older, younger)
    else:
        return None