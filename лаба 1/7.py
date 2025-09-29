'''
Факториал числа
1. Найти факториал числа 3.
2. Найти факториал числа 5.
3. Найти факториал числа N (N вводится).
4. Найти факториал числа, пока не введут 0.
'''

import math

print(f"Факториал числа 3 {math.factorial(3)}")
print(f"Факториал числа 5 {math.factorial(5)}")

n = int(input('введите число '))
print(f"Факториал числа n {math.factorial(n)}")

while True:
    n = int(input('введите число '))
    if n == 0:
        break
    print(f"Факториал числа n {math.factorial(n)}")

