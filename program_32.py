class time:
    def __init__(self,hr,mint,sec):
        self.hour=hr
        self.minute=mint
        self.seconds=sec
    def __add__(self,second):
        hr1=self.hour+second.hour
        min1=self.minute+second.minute
        sec1=self.seconds+second.seconds
        if self.minute+second.minute >= 60:
            hr1=hr1+((self.minute+second.minute)//60)
            min1=(self.minute+second.minute)%60
            

        if self.seconds+second.seconds>= 60:
            min1=min1+((self.seconds+second.seconds)//60)
            sec1=(self.seconds+second.seconds)%60
        print("TIME :",hr1,"hrs ",min1,"mins",sec1,"secs")  
 
hour1=int(input("Enter hours:"))
minute1=int(input("Enter  minutes:"))
second1=int(input("Enter  seconds:"))
obj1=time(hour1,minute1,second1)
hour2=int(input("Enter hours:"))
minute2=int(input("Enter  minutes:"))
second2=int(input("Enter  seconds:"))
obj2=time(hour2,minute2,second2)
obj1+obj2
