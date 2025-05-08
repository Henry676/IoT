from datetime import datetime

def calculate_age(birth_date: str) -> int:

    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age