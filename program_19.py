n=int(input("Enter a number"))
sum=0
num=n
while num>0:
    arm=num%10
    sum+=arm**3
    num//=10
if n==sum:
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")
    
