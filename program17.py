print("To check a given year is leap year ornot")
y=int(input("Enter a year"))
if y%400==0 or(y%100!=100 and y%4==0):
    print(y,"is a leap year")
else:
    print(y,"is not a leap year")
   
