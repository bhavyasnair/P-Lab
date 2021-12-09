l1=input("Enter the list of colors:")
l2=input("Enter the second list of colors:")
a=l1.split(' ')
b=l2.split(' ')
print("The color-list1 not contained in color-list2")
for i in a:
  if i not in b:
      print(i)

