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


class Bike(Transport):
    def __init__(self, brand, speed, type_bike):
        super().__init__(brand, speed)
        self.type_bike = type_bike

    def move(self):
        return print(f"Велосипед {self.brand} едет со скростью {self.speed} km/h")

    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed} km/h, Тип велосипеда: {self.type_bike}"


s = Transport('Ferari', 249)
Car1 = Car('Subaru', 186, 5)
Bike1 = Bike('Велосипед', 46, 'Горный')
print(Bike1)
