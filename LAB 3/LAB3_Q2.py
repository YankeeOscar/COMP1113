tool = input("Enter the name of tool: ")
duration = int(input("Enter reservation duration : "))

match tool:
    case "A":
        rate = 5
    case "B":
        rate = 8
    case "C":
        rate = 12
    case "D":
        rate = 15
    case _:
        rate = 0

total = duration * rate
cost = total * 5

match rate:
    case 0:
        print("wrong tier selection")
    case _:
        match duration:
            case 1:
                print(1, "hours spent on", tool, ". Current electrical usage :", rate * 1)
                print("Total electrical consumption is", total, ", cost is", cost, "TL.")
            case 2:
                print(1, "hours spent on", tool, ". Current electrical usage :", rate * 1)
                print(2, "hours spent on", tool, ". Current electrical usage :", rate * 2)
                print("Total electrical consumption is", total, ", cost is", cost, "TL.")
            case 3:
                print(1, "hours spent on", tool, ". Current electrical usage :", rate * 1)
                print(2, "hours spent on", tool, ". Current electrical usage :", rate * 2)
                print(3, "hours spent on", tool, ". Current electrical usage :", rate * 3)
                print("Total electrical consumption is", total, ", cost is", cost, "TL.")
            case 4:
                print(1, "hours spent on", tool, ". Current electrical usage :", rate * 1)
                print(2, "hours spent on", tool, ". Current electrical usage :", rate * 2)
                print(3, "hours spent on", tool, ". Current electrical usage :", rate * 3)
                print(4, "hours spent on", tool, ". Current electrical usage :", rate * 4)
                print("Total electrical consumption is", total, ", cost is", cost, "TL.")
            case 5:
                print(1, "hours spent on", tool, ". Current electrical usage :", rate * 1)
                print(2, "hours spent on", tool, ". Current electrical usage :", rate * 2)
                print(3, "hours spent on", tool, ". Current electrical usage :", rate * 3)
                print(4, "hours spent on", tool, ". Current electrical usage :", rate * 4)
                print(5, "hours spent on", tool, ". Current electrical usage :", rate * 5)
                print("Total electrical consumption is", total, ", cost is", cost, "TL.")
            case _:
                print("wrong duration")