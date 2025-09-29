import random
numbers = [random.randint(-5, 5) for i in range(21)]
print(f'Начальный список: {numbers}')
print(f'Cписок чётных элементов: {[numbers[x] for x in range(len(numbers)) if numbers[x] % 2 == 0]}')