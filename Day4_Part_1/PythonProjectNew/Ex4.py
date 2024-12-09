def listEx():
    names = ["Debashis", "Utkarsh", "Jashwanthi", "Nivetha"]
    try:
        print(names[10])
    except IndexError:
        print("Array Size is Small...")
    except:
        print("Some Error Occurred")
    else:
        print("No Exception in this Code...")
    finally:
        print("Program by Prasanna")

listEx()