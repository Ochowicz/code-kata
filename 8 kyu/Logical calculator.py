def logical_calc(array, op):
    if op == 'AND':
        for i in range(1, len(array)):
            array[i] = array[i-1] and array[i]
        return array[-1]
    elif op == 'OR':
        for i in range(1, len(array)):
            array[i] = array[i-1] or array[i]
        return array[-1]
    elif op == 'XOR':
        for i in range(1, len(array)):
            array[i] = array[i-1] ^ array[i]
        return array[-1]