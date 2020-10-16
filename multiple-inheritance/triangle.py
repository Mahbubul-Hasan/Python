from polygon import Polygon
from color import Color

class Triangle(Polygon, Color):
    
    def area(self):
        return ((self.getWeight() * self.getHeigth()) / 2)