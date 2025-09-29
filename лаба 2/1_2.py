'''
сумма нечёт чисел от 1 до 100
'''
total = 0
for num in range(1, 99, 2):
    total += num
print(f"Сумма нечетных чисел от 1 до 100 равна: {total}")
