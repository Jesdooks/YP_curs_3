numbers = []

for i in range(5):
    n = int(input(f"Введите число {i+1}: "))
    numbers.append(n)

numbers.sort()
print("Отсортированный список:", numbers)
