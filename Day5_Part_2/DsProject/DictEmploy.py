import operator


class Employ:
    def __init__(self, empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employ No {self.empno}  Employ Name {self.name}  Salary {self.salary}"


e1 = Employ(1, "Debashis",82244)
e2 = Employ(2, "Arjit",88233)
e3 = Employ(3,"Manoj",88211)
employs = [e1, e2, e3]
employs.sort(key=operator.attrgetter("name"))
dct={}
for e in employs:
    dct[e.name] = e.salary

print(dct)