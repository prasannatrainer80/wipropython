import pandas as pd
import numpy as np

class Employ:
    def __init__(self,empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employ No {self.empno}  Employ Name {self.name}  Salary {self.salary}"

e1=Employ(1, "Sindhu", 88233)
e2=Employ(2,"Arjit",88222)
e3=Employ(3,"Yashpal",889099)
e4=Employ(4,"Debashis",90002)
e5=Employ(5,"Utkarsh",98822)

pd.set_option('display.max_columns',None)
info={"1":[e1],"2":[e2],"3":[e3]}
res=pd.DataFrame({"1":[e1],"2":[e2],"3":[e3],"4":[e4],"5":[e5]},index=[1])
res1=pd.DataFrame({"1":[e1]}, index=[0])
print(res)