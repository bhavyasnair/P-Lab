class bank:
    balance=0
    def __init__(self,accountno,name,accounttype,balance):
        self.accountno=accountno
        self.name=name
        self.accounttype=accounttype
        self.balance=balance

    def account_info(self):
        print("\n---ACCOUNT INFORMATION---\n")
        print("Account Number :",self.accountno)
        print("Account Name   :",self.name)
        print("Account Type   :",self.accounttype)
        print("Account Balance:",self.balance,".00")
        print("---------------------------------------")

    def deposit(self):
        deposit=int(input("\nEnter the amount to be deposited"))
        print("Rs.",deposit,"deposited successfully into your account ",self.accountno )
        print("---------------------------------------")
        self.balance=self.balance+deposit

    def withdraw(self):
        withdraw=int(input("\nEnter the amount for withdrawal"))
        if withdraw > self.balance :
            print("Insufficient balance !!!!")
            print("---------------------------------------")
        else:
            self.balance=self.balance-withdraw
            print("Rs.",withdraw,"withdrawn successfully from account",self.accountno)
            print("---------------------------------------")

print("Enter the details of your bank account \n")
acc_no=int(input("Enter the account no:"))
acc_name=input("Enter the account name:")
acc_type=input("Enter account type-(SAVINGS?CURRENT):")
balance=int(input("Enter the initial balance:"))
obj=bank(acc_no,acc_name,acc_type,balance)
while(1):
    print("\n-----------------WElCOME-------------------")
    print("\n1.Account Information\n2.Deposit\n3.Withdrawal\n4.Exit\n")
    opt=int(input("Enter your choice" ))
    if opt==1:
        obj.account_info()
    elif opt==2:
        obj.deposit()
    elif opt==3:
        obj.withdraw()
    elif opt==4:
        print("Thank You ,Visit again\n")
        break
    else:
        print("Invalid option!!!!")
