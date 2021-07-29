class Students:
    def __init__(self,name,rollno,adminno):
        self.myName=name
        self.myRollno=rollno
        self.myAdminno=adminno

obj=[]
                                              #list of objects
obj.append(Students("tamil",68,6789))
obj.append(Students("sharmi",69,6799))
obj.append(Students("sona",70,6766))
print(obj[0].myName,obj[1].myName,obj[2].myName)
print(obj[0].myRollno,obj[1].myRollno,obj[2].myRollno)
print(obj[0].myAdminno,obj[1].myAdminno,obj[2].myAdminno)