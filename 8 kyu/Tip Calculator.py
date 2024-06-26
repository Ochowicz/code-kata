def calculate_tip(amount, rating):
    tips = {
        "terrible": 0,
        "poor": 5,
        "good": 10,
        "great": 15,
        "excellent": 20
    }
    return (tips[rating.lower()] * amount + 99)// 100 if rating.lower() in tips else 'Rating not recognised'