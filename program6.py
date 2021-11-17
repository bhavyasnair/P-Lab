a=input("Enter numbers:")
b=a.split(' ')
c=list(map(int,b))
print("List of numbers:",c)
print(len(c))
l2=[]
for i in range(0,len(c)):
   
   if(c[i]%2!=0):
    
     l2.append(c[i]) 	
  
print("The new list after removing even numbers:",l2)


