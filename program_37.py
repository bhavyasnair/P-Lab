import csv
names=['ROLLNO','NAME','COURSE']
data=[{'ROLLNO':101,'NAME':'Bhavya','COURSE':'MCA'},{'ROLLNO':102,'NAME':'Thanziya','COURSE':'MCA'},{'ROLLNO':103,'NAME':'Siyana','COURSE':'MCA'}]
with open('Details.csv','w',newline="")as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=names)
    writer.writeheader()
    writer.writerows(data)
with open('Details.csv','r')as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)
