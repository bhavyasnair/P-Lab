l1=input("Enter the numbers:")
b=l1.split(',')
c=list(map(int,b))
print("List of numbers:",c)
l2=[i for i in c if i>0]
print("list of positive number is:",l2)
