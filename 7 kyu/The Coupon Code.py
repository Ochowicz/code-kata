from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is not correct_code:
        return False

    expiration_date_obj = datetime.strptime(expiration_date, "%B %d, %Y")
    current_date_obj = datetime.strptime(current_date, "%B %d, %Y")

    if current_date_obj <= expiration_date_obj:
        return True
    else:
        return False