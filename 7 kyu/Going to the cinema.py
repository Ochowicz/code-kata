import math

def movie(card, ticket, perc):
    cost_A = 0
    cost_B = card
    n = 0

    while True:
        n += 1
        cost_A += ticket
        cost_B += ticket * (perc ** n)

        if math.ceil(cost_B) < cost_A:
            return n