stroka = input("Введите строку: ").lower()

char_index = {}

for i, ch in enumerate(stroka):
    if ch not in char_index:
        char_index[ch] = i

print(char_index)
