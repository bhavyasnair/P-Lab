dict_names={}
n=int(input("Enter the number of elements"))
for i in range(1,n+1):
    key=input("Enter the key:")
    value=input("Enter the value:")
    dict_names[key]=value
print(dict_names)
print("The dictionary sorted in ascending order")
print(sorted(dict_names.items()))
print("The dictionary sorted in descending order")
print(sorted(dict_names.items(),reverse=1))
