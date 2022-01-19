n=int(input("Enter a number"))
if n>1:
    for i in range(2,int (n/2)+1):
        if (n%i)==0:
            print("Entered number is not prime")
        else:
            print("Entered number is prime")
            break
else:
    print("Entered number is not prime")
