def words(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if(len(i)>max1):
            max1=len[i]
            temp=i
    print("The longest word count is:",max1)
n=input("Enter ist of words")
a=list(n.split(','))
print(a)
words(a)
