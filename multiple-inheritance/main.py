from rectangle import Rectangle
from triangle import Triangle

rec = Rectangle()
rec.setValues(50, 40)
rec.setColor("Black")
print(rec.area())
print(rec.getColor())

print("--------------------------")

tri = Triangle()
tri.setValues(50, 40)
tri.setColor("Red")
print(tri.area())
print(tri.getColor())
