from math import factorial  
def strong_num(number):
    return 'STRONG!!!!' if number == sum(factorial(int(i)) for i in str(number)) else 'Not Strong !!'