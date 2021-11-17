a=input("Enter elements in a")
b=input("Enter elements in b")
l1=a.split(' ')
c=list(map(int,l1))
l2=b.split(' ')
d=list(map(int,l2))
for i in range(0,len(d)):
  if(c[i] in d):
    print("This value occurs in both the list:",c[i])
    
