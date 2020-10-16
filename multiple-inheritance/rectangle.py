from polygon import Polygon
from color import Color

class Rectangle(Polygon, Color):

    def area(self):
        return self.getHeigth() * self.getWeight()