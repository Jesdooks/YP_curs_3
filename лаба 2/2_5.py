print('Введите значения списка через пробел: ')
spis = list(map(int, input().split()))

if len(spis) > 1:
    spis[0], spis[-1] = spis[-1], spis[0]
    print(spis)
else:
    print('Должно быть от двух значений. Введите новый список!')


