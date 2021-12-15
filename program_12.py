l1=input("Enter the word:")
b=list(l1)
print("List of letters:",b)
vowels=['a','e','i','o','u']
l2=[j for j in b if j in vowels]
print("The list of vowels in the entered word are:",l2)
