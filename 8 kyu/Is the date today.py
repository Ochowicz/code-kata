from datetime import datetime

def is_today(date):
    today = datetime.today().date()
    date = date.date()
    return today == date