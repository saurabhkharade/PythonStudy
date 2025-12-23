day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")


choice = int(input("Enter choice (1-3): "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("Update")
    case 3:
        print("Delete")
    case _:
        print("Wrong choice")
