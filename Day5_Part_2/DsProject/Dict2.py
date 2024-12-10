class Employ:
    def __init__(self, empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employ No {self.empno} Employ Name {self.name} Salary {self.salary}"

e1=Employ(1, "Debashis",88323)
e2=Employ(2,"Utkarsh",88112)
e3=Employ(3,"Bala",88111)
dict={}
dict["1"]=e1
dict["2"]=e2
dict["3"]=e3

print("First Employ Data ", dict["1"])
print("Second Employ Data ", dict["2"])
print("Third Employ Data  ", dict["3"])