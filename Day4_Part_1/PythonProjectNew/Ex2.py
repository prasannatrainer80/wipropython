def division():
    try:
        a = int(input("Enter First Number   "))
        b = int(input("Enter Second Number  "))
        c = a / b
        print("Division ", c)
    except ZeroDivisionError:
        print("Division by Zero impossible...")
    except ValueError :
        print("String Cannot be Converted as Integer")
    else:
        print("This Code don't have any runtime error...")
    finally:
        print("Program from Great Learning Prasanna Batch")

division()