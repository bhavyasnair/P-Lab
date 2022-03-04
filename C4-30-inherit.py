class employee:
    def __init__(self,empid,name,salary,address):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.address=address
    def display(self):
        print("\nEMPLOYEE ID",self.empid,"\nNAME",self.name,"\nSALARY",self.salary,"\nADDRESS",self.address)
class teacher(employee):
    def __init__(self,empid,name,salary,address,department,subjects_taught):
        self.department=department
        self.subjects_taught=subjects_taught
        employee.__init__(self,empid,name,salary,address)

    def display(self):
        print("\nEMPLOYEE ID",self.empid,"\nNAME",self.name,"\nSALARY",self.salary,"\nADDRESS",self.address,"\nDEPARTMENT",self.department,"\nSUBJECTS TAUGHT",self.subjects_taught)
a=employee("e123","arya","45000","chathanpalli")
a.display()
b=teacher("t123","fathima","78000","kalamassery","mca","AI")
b.display()
