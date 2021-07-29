class Department:
    def __init__(self,deptname):
        self.deptname=deptname
    def addStud(self,name,rollno,address,clgname,mblno):
        print(name,rollno,address,clgname,mblno,self.deptname)

# d=Department("ECE")
# d.addStud("tamilarasi",68,"cuddalore","IFET",9876543210)
# d=Department("CSE")
# d.addStud("sharmi",46,"cuddalore","IFET",9876432178)     
Departmentname=input("Enter 1st dept name:")
d=Department(Departmentname)
name1=input("enter name:")
rollno1=int(input("Enter roll no.:"))
address1=input("Enter address:")
clgname1=input("Enter clg name:")
mblno1=int(input("Enter the mblno.:"))
Departmentname=input("Enter 2nd dept name:")
e=Department(Departmentname)
name2=input("enter name:")
rollno2=int(input("Enter roll no.:"))
address2=input("Enter address:")
clgname2=input("Enter clg name:")
mblno2=int(input("Enter the mblno.:"))
d.addStud(name1,rollno1,address1,clgname1,mblno1)
e.addStud(name2,rollno2,address2,clgname2,mblno2)
 