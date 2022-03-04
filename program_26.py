import math
ar_Rect=lambda l,b : l*b
ar_Square=lambda a: a*a
ar_Triangle=lambda x,y: 0.5*x*y
ll,bb=map(int,input("Enter the length and breadth of rectangle").split())
s=int(input("Enter the side length of square"))
hh,bs=map(int,input("Enter the height and base of triangle").split())
print("Area of square is ",ar_Square(s))
print("Area of rectangle is ",ar_Rect(ll,bb))
print("Area of triangle is ",ar_Triangle(hh,bs))


