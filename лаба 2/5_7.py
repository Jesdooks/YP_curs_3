names = ['Анна', 'Иван', 'Мария', 'Иван', 'Сергей', 'Анна', 'Анна']
name_b_1 = {}
k = 0
#i, j - указатели
for i in names:
    for j in names:
        if i == j:
            k += 1
            name_b_1[i] = k
    k = 0

max_prod = max(name_b_1, key=name_b_1.get)
duplicates = [name for name, count in name_b_1.items() if count > 1]
print('Имена, которые встречаются более одного раза: ', ', '.join(duplicates))
print(f"Имя, которое встречается чаще всего: {max_prod}, кол-во: {name_b_1[max_prod]}")
