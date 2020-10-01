class Car():
    pass


ford = Car()
ford.speed = 200
ford.color = "black"

print(ford.speed)
print(ford.color.capitalize())


class Vehicle():
    def __init__(self):
        print("__init__ method call")


car = Vehicle()
car.speed = 200
car.color = "black"

print(car.speed)
print(car.color.capitalize())


class SuperCar():
    def __init__(self, speed, color):
        print(speed)
        print(color)


honda = SuperCar(500, "Red")


class Bike():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color


yamaha = Bike(150, "black")

print(yamaha.speed)
print(yamaha.color.upper())
