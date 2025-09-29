'''
Сумма чисел в диапазоне
1. Найти сумму чисел от 1 до 10.
2. Найти сумму чисел от 1 до N (N вводится).
3. Найти сумму чётных чисел от 1 до N.
4. Найти сумму нечётных чисел от 1 до N.
'''

sum_1_10 = sum(range(1, 10))
print("Сумма чисел от 1 до 10:", sum_1_10)

n = int(input("Введите число N: "))
sum_1_n = sum(range(1, n))
print(f"Сумма чисел от 1 до {n}:", sum_1_n)

sum_chetnoe = sum(i for i in range(2, n, 2))
print(f"Сумма чётных чисел от 1 до {n}:", sum_chetnoe)

sum_odd_ne_chetnoe = sum(i for i in range(1, n, 2))
print(f"Сумма нечётных чисел от 1 до {n}:", sum_odd_ne_chetnoe)
