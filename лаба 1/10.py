'''
Циклы с условием
1. Вводить числа, пока не введут 0, и посчитать их сумму.
2. Вводить числа, пока не введут отрицательное, и посчитать количество введённых.
3. Вводить числа, пока не введут чётное, и вывести сумму нечётных.
4. Вводить числа, пока не введут число больше 100, и вывести среднее
арифметическое.
'''
total_sum = 0
while True:
    num = int(input('введите число '))
    if num == 0:
        break
    total_sum += num
print(f"Сумма введённых чисел {total_sum}")

count = 0
while True:
    num = int(input('введите число '))
    if num < 0:
        break
    count += 1
print(f"кол-во введённых чисел {count}")

odd_sum = 0
while True:
    num = int(input('введите число '))
    if num % 2 == 0:
        break
    odd_sum += num
print(f"Сумма нечётных чисел {odd_sum}")

total = 0
count = 0
while True:
    num = int(input('введите число '))
    if num > 100:
        break
    total += num
    count += 1
print(f"Среднее арефметическое: {total / count}") if count > 0 else 0

