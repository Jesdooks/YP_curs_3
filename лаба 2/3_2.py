text = input("Введите строку: ")

slovar = {}

for char in text:
    if char.isalpha():  # Считаем только буквы
        if char in slovar:
            slovar[char] += 1
        else:
            slovar[char] = 1

print(slovar)
