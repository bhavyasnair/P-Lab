class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        area=self.length*self.breadth
        print("Area of rectangle:",area)
        return(area)
    def perimeter(self):
        perimeter=2*(self.length+self.breadth)
        print("perimeter of rectangle:",perimeter)

print("Rectangle 1")
obj1=rectangle(40,20)
a1=obj1.area()
obj1.perimeter()
print("\nRectangle 2")
obj2=rectangle(30,20)
a2=obj2.area()
obj2.perimeter()
if a1>a2 :
    print("\n Rectangle 1 is larger than Rectangle 2 !")
elif a1==a2:
    print("\n Both have the same area !")
else:
    print("\n Rectangle 2 is larger than Rectangle 1 !")
