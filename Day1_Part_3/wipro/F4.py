def add(x, y):
    return x+y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

x=int(input("Enter First Number   "))
y = int(input("Enter Second Number   "))
print("Sum of {} and {} is {}".format(x, y, add(x,y)))
print("Sub of {} and {} is {}".format(x, y, sub(x,y)))
print("Mult of {} and {} is {}".format(x, y, mult(x,y)))

