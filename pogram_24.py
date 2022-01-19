def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
n=int(input("Enter the number whose factor has to be found out:"))
factor(n)
