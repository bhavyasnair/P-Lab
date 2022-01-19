def fib(x):
 if x<=1:
     return x
 else:
     return(fib(x-1)+fib(x-2))
n=int(input("Enter the limit"))
print("Fibonaaci sequence")
for i in range(0,n):
  print(fib(i))

   
