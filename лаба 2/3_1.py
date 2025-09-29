students = {
    'Андрей': [2, 5, 3],
    'Никита': [2, 2, 4],
    'Егор': [4, 4, 5],
    'Ольга': [5, 5, 5]
}

for name, mark in students.items():
    sr = sum(mark) / len(mark)
    print(f"Средний балл студента {name}: {sr:.2f}")
