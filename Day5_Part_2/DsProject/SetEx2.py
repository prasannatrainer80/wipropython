names = {"Raj", "Manoj", "Kishore", "Sekhar", "Raj", "Manoj", "Kishore", "Sekhar", "Raj", "Manoj", "Kishore", "Sekhar"}
def show():
    for n in names:
        print(n)

def add(name):
    names.add(name)

def remove(name):
    names.discard(name)

def exists(name):
    if name in names:
        print(f"{name} is Present in the list")
    else:
        print(f"{name} is not present in the list")

show()
add("Debashis")
show()
remove("Raj")
print("*** After Discard *** ")
show()
exists("Debashis")
