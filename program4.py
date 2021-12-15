a=input("Enter numbers:")
b=a.split(',')
c=list(map(int,b))
print("List of numbers:",c)
n=len(c)
for i in range(n):
   if(c[i]>100):
      c[i]='over'
print(c)

