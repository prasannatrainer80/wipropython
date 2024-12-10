def show():
    list2 = ["Rucha", "Mohan", "Sanjay", "Prasanth","Arjit","Bala","Lakshmi"]
    list2.sort()
    print(list2)

    list3 = [12,4,22,88,23,11,82,112]
    list3.sort()
    print(list3)

    list4 = sorted(list2, reverse=True)
    print(list4)

    names = ["Rucha", "Mohan", "Sanjay", "Prasanth","Arjit","Bala","Lakshmi","nivedha","yashpal","Nivedha","aman","rucha"]
    res=sorted(names,reverse=False)
    print(res)
    names.sort(key=str.lower)
    print(names)
show()