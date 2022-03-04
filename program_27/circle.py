from graphics import rectangle
from graphics import circle
from graphics.threeD_graphics import cuboid
from graphics.threeD_graphics import sphere

l = int(input("enter the length of the rectangle"))
b = int(input("enter the breadth of the rectangle"))
rectangle.area(l,b)
rectangle.perimeter(l,b)
print()
r = int(input("enter the radius of the circle"))
circle.area(r)
circle.perimeter(r)
print()
l = int(input("enter the length of the cuboid"))
b = int(input("enter the breadth of the cuboid"))
h = int(input("enter the height of the cuboid"))
cuboid.area(l,b,h)
cuboid.perimeter(l,b,h)
print()
r = int(input("enter the radius of the sphere"))
sphere.area(r)
sphere.volume(r)
