class ConEx2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "First No " +str(self.a)+" Second No "+str(self.b)

c1=ConEx2(12,5)
print(c1)