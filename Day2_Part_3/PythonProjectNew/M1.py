import Employ as employ

class Demo:
    def display(self,employList):
        for employ in employList:
            print(employ)

    def show(self,*employs):
        for employ in employs:
            print(employ)

e1=employ.Employ(1,"Raj",88233)
e2=employ.Employ(2,"Mahesh",82333)
e3=employ.Employ(3,"Nalini",81122)
e4=employ.Employ(4,"Rajan",88112)

employList = [e1, e2, e3, e4]

demo=Demo()
demo.show(e1,e2,e3,e4)
demo.display(employList)