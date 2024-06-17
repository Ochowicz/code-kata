def alphabet_war(fight):
    left_letters_and_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_letters_and_power = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    sum_left = 0
    sum_right = 0
    for letter in fight:
        sum_left += left_letters_and_power.get(letter, 0)
        sum_right += right_letters_and_power.get(letter, 0)
    return 'Left side wins!' if sum_left > sum_right else 'Right side wins!' if sum_left < sum_right else "Let's fight again!"