set1 = input("Введите текст: ").lower()
words = set1.split()

new_set = set(words)

print(f"Уникальные слова в тексте: {new_set}")
