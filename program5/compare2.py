a=input("Enter elements in a")
b=input("Enter elements in b")
l1=a.split(' ')
c=list(map(int,l1))
l2=b.split(' ')
d=list(map(int,l2))
sum1=0
for i in range(0,len(c)):
   sum1+=c[i]
print("SUM of values in first list:",sum1)
sum2=0
for j in range(0,len(d)):
   sum2+=d[j]
print("SUM of values in second",sum2)
if(sum1==sum2):
  print("The list sums up to same value")
else:
  print("The sums of the lists are different")
