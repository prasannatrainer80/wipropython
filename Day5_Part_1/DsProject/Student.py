import operator


class Student:
    def __init__(self,sid,sname,city,cgp):
        self.sid = sid
        self.sname = sname
        self.city = city
        self.cgp = cgp

    def __str__(self):
        return (f"Student Id {self.sid} Student Name {self.sname} "
                f" City  {self.city}  Cgp  {self.cgp}")

s1=Student(1,"Debhashis","Delhi",8.2)
s2=Student(2,"Arjit","Hyderabad",9.2)
s3=Student(3,"Sravanthi","Chennai",9.1)
s4=Student(4,"Utkarsh","Pune",8.7)
students = [s1, s2, s3, s4]
for s in students:
    print(s)

print("Sorting Data w.r.t. Student Name Wise  ")
students.sort(key=operator.attrgetter("sname"))
# print(students)
for s in students:
    print(s)
# results = sorted(students,key=s1.sname)
# for s in results:
#     print(s.sid)
