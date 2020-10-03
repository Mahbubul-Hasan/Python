class Polygon:
    __height = None
    __width = None

    def setValues(self, height, width):
        self.__height = height
        self.__width = width

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width


class Rectangle(Polygon):
    def area(self):
        return self.getHeight() * self.getWidth()


class Triangle(Polygon):
    def area(self):
        return self.getHeight() * self.getWidth() / 2


rec = Rectangle()
rec.setValues(50, 40)
print(rec.area())

tri = Triangle()
tri.setValues(50, 40)
print(tri.area())
