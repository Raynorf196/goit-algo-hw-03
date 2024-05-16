from datetime import datetime
import random


def get_days_from_today(date):
    date_convert = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.now()
    result = current_date - date_convert
    return result.days

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    return sorted(list(numbers))
