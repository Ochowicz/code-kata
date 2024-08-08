def jumping_number(number):
    return "Jumping!!" if all(abs(int(i) - int(j)) == 1 for i, j in zip(str(number), str(number)[1:])) else "Not!!"