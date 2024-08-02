def product_array(numbers):
    def iloczyn(numbers):
        result = 1
        for i in numbers:
            result *= i
        return result
    return [iloczyn(numbers)/i for i in numbers]