from polygon import Polygon


class Rectangle(Polygon):
    def area(self):
        return self.getHeight() * self.getWidth()
