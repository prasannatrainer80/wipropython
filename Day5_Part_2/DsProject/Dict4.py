student_info=dict(name="Debashis",age=21,company="Wipro",city="Delhi")
print(student_info)
print("Printing Keys  ")
for key in student_info.keys():
    print(key)

print("Printing Values  ")
for value in student_info.values():
    print(value)
print("Both Keys and Values   ")
for key, value in student_info.items():
    print(key, "   ", value)