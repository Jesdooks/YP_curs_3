from datetime import datetime

# Получить текущую дату и время
now = datetime.now()

# Полная дата и время
print("Текущая дата и время:", now)

# Только текущая дата
print("Текущая дата:", now.date())

# Только текущее время
print("Текущее время:", now.time())
