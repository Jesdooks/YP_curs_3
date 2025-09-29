from datetime import datetime


def format_datetime_rus(dt):
    days = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }

    months = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря"
    }

    day_name = days[dt.weekday()] #dt.weekday - возв номер дня нед и по нему возв название дня
    day = dt.day
    month_name = months[dt.month] #dt.month - возв номер месяца и по нему возв название месяца
    year = dt.year #dt.year - возв год
    time_str = dt.strftime("%H:%M") #dt.strftime - возв время в формате %H:%M

    return f"{day_name} {day} {month_name} {year} года, время: {time_str}"


# Пример использования
now = datetime(2025, 11, 26, 5, 30)
formatted = format_datetime_rus(now)
print(formatted)
