dict1={}
dict2={}
n1=int(input("Enter the numberof elements in first dict"))
n2=int(input("Enter the numberof elements in second dict"))
for i in range(0,n1):
   k=input("Enter the key")
   v=input("Enter the value")
   dict1[k]=v
print(dict1)
for i in range(0,n2):
   k=input("Enter the key")
   v=input("Enter the value")
   dict2[k]=v
print(dict2)
dict2.update(dict1)
print("The merged dictionary is:",dict2)
 
