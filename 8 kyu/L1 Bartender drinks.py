def get_drink_by_profession(param):
    drink_preferences = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
}
    return drink_preferences[param.lower()] if param.lower() in drink_preferences else 'Beer'