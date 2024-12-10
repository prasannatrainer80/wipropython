import operator


class Employ:
    def __init__(self,empno,name,salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employ No {self.empno}  Employ Name {self.name}  Salary {self.salary}"

e1 = Employ(1,"Debashis",88222)
e2 = Employ(2,"Arjit",88112)
e4=Employ(4,"Utkarsh",88155)
e5=Employ(5,"Karthik",99999)
e3 = Employ(3,"Sravanthi",88111)

employs = [e1, e2, e3, e4, e5]
for e in employs:
    print(e)

employs.sort(key=operator.attrgetter("name"))
print("Sort By Name-wise  ")
for e in employs:
    print(e)

employs.sort(key=operator.attrgetter("salary"),reverse=True)
print("Sort By Salary Descending Order  ")
for e in employs:
    print(e)