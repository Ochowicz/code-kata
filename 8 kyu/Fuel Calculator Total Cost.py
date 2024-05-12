# In this kata you will have to write a function that takes litres and price_per_litre (in dollar) as arguments.
#
# Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per litre cannot be more than 25 cents. Return the total cost rounded to 2 decimal places. Also you can guess that there will not be negative or non-numeric inputs.
def fuel_price(litres, price_per_litre):
    if litres >= 10:
        n = 5
    elif litres >= 8:
        n = 4
    elif litres >= 6:
        n = 3
    elif litres >= 4:
        n = 2
    elif litres >= 2:
        n = 1
    else:
        n = 0
    sum = litres * (price_per_litre - 0.05 * n)
    return round(sum, 2)