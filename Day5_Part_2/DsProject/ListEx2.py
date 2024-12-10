def show():
    list1 = ["Prasanna","Rajesh","Nissy","Abhi"]
    list2 = ["Rucha","Mohan","Sanjay","Prasanth"]
    print(list1+list2)
    print(list1 * 2)
    print("Prasanna" in list1)
    print("Mohan" in list2)
    print("Bala" in list2)

    list3 = list1.copy()
    print(list3)
    list4 = list2.reverse()
    print(list4)
show()