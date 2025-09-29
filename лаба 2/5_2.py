elements = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

slovar = {}
for i in elements:
    slovar[i] = slovar.get(i, 0) + 1

print(f'Итоговый словарь: {slovar}')
