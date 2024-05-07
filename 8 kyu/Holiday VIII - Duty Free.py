def duty_free(price, discount, holiday_cost):
    return int(holiday_cost / (discount/100) / price) if discount != 0 and price != 0 else 'Division 0 Error'