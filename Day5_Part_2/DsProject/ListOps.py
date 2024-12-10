names=["Nandini","Thrisha","Bala","Debashis","Utkarsh"]

def addItem(name):
    names.append(name)

def push(pos,name):
    names.insert(pos,name)

def modify(pos,name):
    names[pos] = name

def delete(name):
    names.remove(name)

def showAll():
    for i in names:
        print(i)

def search(item):
    flag = False
    for i in names:
        if i==item:
            print("Element Found ")
            flag = True
            break
    if flag==False:
        print("Element Not Found")

showAll()
newName=input("Enter Name  ")
addItem(newName)
showAll()
newName=input("Enter Name to Insert  " )
pos=int(input("Enter Position to Insert  "))
push(pos, newName)
showAll()
updName=input("Enter Name to Update   ")
pos=int(input("Enter the Position to modify  "))
modify(pos,updName)
showAll()
delName=input("Enter Name to Remove   ")
delete(delName)
showAll()
searchName =input("Enter Name to Search  ")
search(searchName)