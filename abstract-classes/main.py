from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

square = Square(5)

print(square.area())
print(square.perimeter())
