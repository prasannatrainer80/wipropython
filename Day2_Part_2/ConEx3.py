class Employ:
    def __init__(self,empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return "Employ No "+str(self.empno) + " Employ Name " +str(self.name) + " Salary " +str(self.salary)

e1=Employ(1, "Debhasis",88323.23)
print(e1)
e2=Employ(2,"Sindhu",99234.22)
print(e2)