import random

spis = [random.randint(1, 10) for i in range(20)]

n = set(spis)

print("Случайные числа:", spis)
print("Уникальные числа:", n)
