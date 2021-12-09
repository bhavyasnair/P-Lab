a=int(input("Enter a number"))
b=int(input("Enter second number"))
temp=0
gcd=0
if a>b:
    temp=b
    b=a
    a=temp
for i in range(1,b):
    if(a%i==0 and b%i==0):
        gcd=i
print("GCD of 2 numbers is:",gcd)
