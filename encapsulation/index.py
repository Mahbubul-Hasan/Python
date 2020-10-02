class Rectangular():

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def area(self):
        return self.__height * self.__width


rec = Rectangular()
rec.set_height(15)
rec.set_width(20)
print(rec.area())
