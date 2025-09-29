words = ["python", "Java", "c++", "Rust", "go"]
print("Все слова в верхнем регистре и длина слова больше 3 символов:", *[x.upper() for x in words if len(x) > 3])