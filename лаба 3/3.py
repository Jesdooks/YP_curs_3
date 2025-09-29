def Countdown(n):
    while n > 0:
        yield n
        n -= 1

#yield тоже самое что и return только сохраняя все локальные переменные и позицию выполнения
for x in Countdown(5):
    print(x)
