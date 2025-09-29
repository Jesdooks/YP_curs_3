import random
numbers = [random.randint(-5, 5) for i in range(21)]
print(f'Начальный список: {numbers}')
print(f'Максимальное значение: {max(numbers)} \nМинимальное значение:{min(numbers)}')