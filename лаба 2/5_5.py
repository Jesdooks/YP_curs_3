spis = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7, 8]

new_spis = []
set_1 = set()
for i in spis:
    if i not in set_1:
        set_1.add(i)

for i in set_1:
    if i not in new_spis:
        new_spis += [i]

print("Исходный список:", spis)
print("Список без дубликатов с сохранением порядка:", new_spis)
