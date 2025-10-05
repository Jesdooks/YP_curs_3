class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        return print(f"Транспорт едет со скоростью {self.speed} km/h")

    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed} km/h"


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        return print('Beep beep!')

    def move(self):
        return print(f"Машина {self.brand} едет со скоростью {self.speed} km/h")

    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed} km/h, Кол-во мест: {self.seats}"

    #задание 3
    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented

class Bike(Transport):
    def __init__(self, brand, speed, type_bike):
        super().__init__(brand, speed)
        self.type_bike = type_bike

    def move(self):
        return print(f"Велосипед {self.brand} едет со скростью {self.speed} km/h")

    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed} km/h, Тип велосипеда: {self.type_bike}"


Transport1 = Transport('Ferari', 249)
Transport1 = Transport('Mclaren', 351)

Car1 = Car('Subaru', 186, 5)
Car2 = Car('Porshe', 255, 2)

Bike1 = Bike('Чемпион', 46, 'Горный')
Bike1 = Bike('Stels', 67, 'Гоночный')

print(Transport1)
print(Transport1)
print(Car1)
print(Car2)
print(Bike1)
print(Bike1)
print(f"------------------------------------------------------------------")

print("Метод move:")
Transport1.move()
Car1.move()
Bike1.move()

print(f"------------------------------------------------------------------")
print("Метод honk:")
Car1.honk()
Car2.honk()

print(f"------------------------------------------------------------------")
print("Метод len у Car:")
print(f"Кол-во сиденьев в car1: {len(Car1)}")
print(f"Кол-во сиденьев в car2: {len(Car2)}")

print(f"------------------------------------------------------------------")
print("Сравнение машин по скорости (метод eq у Car):")
print(f"Скрость первоый и второй машины равна? {Car1 == Car2}")

print(f"------------------------------------------------------------------")
print("Сложение скоростей двух машин (метод add у Car):")
print(f"Сумма скоростей: {Car1 + Car2}")

print(f"------------------------------------------------------------------")
print("Сложение скрости машины и велосипеда:")
try:
    print(f"Сумма скростей машины и велосипеда: {Car1 + Bike1}")
except TypeError as e:
    print("Ошибка - в классе Car используется метод add, \nкоторый поддерживает сложение только с объектами класса Car:")

print(f"------------------------------------------------------------------")
print('Принцип полиморфизма:')
vehicles = [Transport1, Car1, Bike1]
for v in vehicles:
    v.move()


#isinstance(obj, Class) — функция проверяет, является ли объект obj экземпляром класса Class
#NotImplemented - специальное значение, которое возвращается если операция не поддерживается для такого типа
#eq - возращает True False, равно
#полиморфизма - вызов метода move() работает для всех объектов независимо от класса