class Customer:
    def __init__(self,custId,custName,billAmounts):
        self.custId = custId
        self.custName = custName
        self.billAmounts = billAmounts
        self.sum = 0
        self.avg = 0

    def __str__(self):
        self.sum = sum(self.billAmounts)
        self.avg = self.sum / len(self.billAmounts)
        return f"Customer Id {self.custId} Customer Name {self.custName} Sum  {self.sum}  Average {self.avg}"

custId1=int(input("Enter Customer Id  "))
custName = input("Enter Customer Name  ")
billAmount1=float(input("Enter Bill Amount 1  "))
billAmount2 = float(input("Enter Bill Amount 2  "))
billAmount3 = float(input("Enter Bill Amount 3  "))
bills1 = [billAmount1, billAmount2, billAmount3]
c1 =Customer(custId1,custName,bills1)
custId1=int(input("Enter Customer Id  "))
custName = input("Enter Customer Name  ")
billAmount1=float(input("Enter Bill Amount 1  "))
billAmount2 = float(input("Enter Bill Amount 2  "))
billAmount3 = float(input("Enter Bill Amount 3  "))
bills2 = [billAmount1, billAmount2, billAmount3]
c2 =Customer(custId1,custName,bills1)
print(c1)
print(c2)