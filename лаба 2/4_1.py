# Создаем два множества
set1 = set(map(int, input('Введите значения первого множества через пробел: ').split()))
set2 = set(map(int, input('Введите значения второго множества через пробел: ').split()))

# Находим пересечение множеств
intersection = set1 & set2

# Находим объединение множеств
union = set1 | set2

print("Множество 1:", set1)
print("Множество 2:", set2)
print("Пересечение:", intersection)
print("Объединение:", union)
