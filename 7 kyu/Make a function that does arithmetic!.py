def arithmetic(a, b, operator):
    operation = {"add": '+', "subtract": '-', "multiply": '*', "divide": '/'}
    return eval(str(a) + operation[operator] + str(b))