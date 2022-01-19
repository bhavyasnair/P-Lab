def pattern(n):
    for i in range(1,n+1):
      print("\n")
      for j in range(1,i+1):
         print(i*j,end=" ")
n=int(input("Enter the number of steps"))
pattern(n)
