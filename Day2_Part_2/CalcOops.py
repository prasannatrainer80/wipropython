class Calculation:
    def set(self,a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

num1 = int(input())
num2 = int(input())
calc=Calculation()

calc.set(num1,num2)
print(calc.sum())
print(calc.sub())
print(calc.mult())
print(calc.div())