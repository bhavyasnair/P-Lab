a=input("Enter a string")
s1=a[0]
a=a.replace(s1,'$')
a=s1+a[1:]
print(a)
