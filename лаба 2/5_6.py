slovar = {
    'яблоки': 50,
    'бананы': 30,
    'виноград': 80,
    'апельсины': 60
}

max_prod = max(slovar, key=slovar.get)

print(f'Исходный словарь: {slovar}')
print(f"Самый дорогой товар: {max_prod}, цена: {slovar[max_prod]}")
