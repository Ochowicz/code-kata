def order_food(lst):
    meal_count = {}
    for programer in lst:
        meal = programer['meal']
        if meal in meal_count:
            meal_count[meal] += 1
        else:
            meal_count[meal] = 1
    return meal_count