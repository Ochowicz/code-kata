def balanced_num(number):
    border = (len(str(number)) - 1) // 2
    return 'Balanced' if border == 0 or sum(int(i) for i in str(number)[:border]) == sum(int(i) for i in str(number)[-border:]) else 'Not Balanced'