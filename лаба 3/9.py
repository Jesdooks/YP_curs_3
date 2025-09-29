from datetime import date, timedelta

# Дата рождения
birth_date = date(2006, 1, 13)

today = date.today()
count_day_do_segodny = (today - birth_date).days

# Следующий день рождения
next_birthday = date(today.year, birth_date.month, birth_date.day)

# Если следующий день рождения уже прошёл в этом году, берем следующий год
if next_birthday < today:
    next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

# Количество дней до следующего дня рождения
days_until_birthday = (next_birthday - today).days

print(f"Дней с рождения: {count_day_do_segodny}")
print(f"Дней до следующего дня рождения: {days_until_birthday}")
