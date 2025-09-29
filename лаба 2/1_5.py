'''
Фибоначи
'''

n = int(input("Введите длину последовательности Фибоначчи: "))

if n <= 0:
    print("Введите положительное число")
elif n == 1:
    print("0")
else:
    a, b = 0, 1
    print(a, b, end=' ')
    for _ in range(3, n + 1):
        c = a + b
        print(c, end=' ')
        a, b = b, c
    print()

