a=input("Enter elements in a")
b=input("Enter elements in b")
l1=a.split(' ')
c=list(map(int,l1))
l2=b.split(' ')
d=list(map(int,l2))
if(len(c)==len(d)):
  print("The lists are of same length")
else:
  print("The lists are in different length")

