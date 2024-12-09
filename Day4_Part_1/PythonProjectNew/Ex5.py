def listEx():
    try:
        names = ["Debashis", "Utkarsh", "Jashwanthi", "Nivetha"]
        for i in range(5):
            print("Name at Index element ",i, " Is ", names[i])
    except IndexError:
        print("Array Size is Small...")
    finally:
        print("Program by Prasanna")

listEx()