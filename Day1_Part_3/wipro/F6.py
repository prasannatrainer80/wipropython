students = ["Arjit","Bala","Sindhu","Sravanthi","Rucha","Debashis","Mithun","Mohan"]

def a_calc(string):
    return len(string)

for i in students:
    print("Student Name {} Length  {}".format(i, a_calc(i)))