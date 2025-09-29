import string

import string

stroka = input("Введите предложение: ").lower()

#string.punctuation список всех знаков препинания
for i in string.punctuation:
    stroka = stroka.replace(i, ' ')

spis = stroka.split()
slovar = {}

for word in spis:
    slovar[word] = slovar.get(word, 0) + 1

print(f'Итоговый список слов и их количества: {slovar}')
