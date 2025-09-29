'''
вывода таблицы умножения от 1 до 9
'''

for i in range(1, 9):
    for j in range(1, 9):
        print(f"{i}x{j}={i*j}", end="\t")
    print()
