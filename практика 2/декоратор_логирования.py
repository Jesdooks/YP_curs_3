def logger(func):
    def s(*args, **kwargs):
        print(f"Вызов функции {func} с аргументами {args} и {kwargs}")
        res = func(*args, **kwargs)
        print(f"Функция {func} вернула {res}")
    return s


@logger
def add(a, b):
    return a+b


@logger
def divide(a, b):
    if b != 0:
        return a / b


@logger
def greet(name):
    return f"Привет {name}"


print("-"*60)
res0 = add(1, 2)
print("-"*60)
res1 = divide(1, 2)
print("-"*60)
res2 = greet("Никитоооооос")


