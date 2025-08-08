try:
    a = int(input("Enter the value for a :: "))

    b = int(input("Enter the value for b :: "))

    print("What kind of opeartions you want to perform.Press + for addition\nPress - for substarction\nPress / for division\nPress * for multiplication.")

    o = input("Enter operation :: ")
    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The result is {a - b}")
        case "/":
            print(f"The result is {a / b}")
        case "*":
            print(f"The result is {a * b}")
        case default:
            print(f"There was an error!!")


except Exception as e:
    print("Enter valid values for a and b!!")
    