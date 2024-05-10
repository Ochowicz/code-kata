# Write function bmi that calculates body mass index (bmi = weight / height2).
#
# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"

def bmi(weight, height):
    #your code here

    bmi = (weight / height**2)
    if bmi <= 18.5:
        msg = "Underweight"
    elif bmi <= 25.0:
        msg = "Normal"
    elif bmi <= 30.0:
        msg = "Overweight"
    elif bmi > 30.0:
        msg = "Obese"
    return msg