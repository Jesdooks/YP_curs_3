print('Введите значения списка через пробел: ')
spis = list(map(int, input().split()))
new_spis = []

for i in spis:
    if i not in new_spis:
        new_spis.append(i)

print(f'Список без повторяющихся элементов: {new_spis}')
