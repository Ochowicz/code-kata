def calculate_age(year_of_birth, current_year):
    past = year_of_birth - current_year
    if past == 1:
        return f"You will be born in {past} year."
    elif past > 0:
        return f"You will be born in {past} years."
    elif past == 0:
        return "You were born this very year!"
    elif past == -1:
        return f"You are {-past} year old."
    else:
        return f"You are {-past} years old."