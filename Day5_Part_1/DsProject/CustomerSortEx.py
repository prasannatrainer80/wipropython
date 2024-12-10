import operator


class Customer:
    def __init__(self,cid,cname,city,billAmount):
        self.cid = cid
        self.cname = cname
        self.city = city
        self.billAmount = billAmount

    def __str__(self):
        return f"Customer Id {self.cid}  Customer Name {self.cname}  City {self.city}  Bill Amount {self.billAmount}"

c1 = Customer(1, "Debashis","Delhi",88822.22)
c2 = Customer(2, "Nivedha","Hyderabad",90000.22)
c3 = Customer(3, "Arjit","Chennai",91122.22)
c4 = Customer(4, "Sravanthi","Delhi",89001.22)
c5 = Customer(5, "Bala","Chennai",92455.22)
c6 = Customer(6, "Sindhu","Hyderabad",98222.22)

customers = [c1, c2, c3, c4, c5, c6]
print("Customer Data is  ")
for c in customers:
    print(c)

customers.sort(key=operator.attrgetter("cname"))
print("Customer Sort By Customer name  ")
for c in customers:
    print(c)

customers.sort(key=operator.attrgetter("billAmount"))
print("Customer Sort By Bill Amount  ")
for c in customers:
    print(c)

customers.sort(key=operator.attrgetter("billAmount"),reverse=True)
print("Customer Sort By Bill Amount Descending Order ")
for c in customers:
    print(c)


customers.sort(key=operator.attrgetter("city","cname"))
print("Customer Sort By Multiple Parameters ")
for c in customers:
    print(c)

