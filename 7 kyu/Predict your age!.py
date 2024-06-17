def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    lst = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    return int((sum(map(lambda x: x ** 2, lst))) ** (0.5) / 2)