computer = input("Enter the computer tier selection: ")
duration = int(input("Enter reservation duration: "))

match computer:
    case "A":
        rate = 2
    case "B":
        rate = 5
    case "C":
        rate = 10
    case "D":
        rate = 15
    case _:
        rate = 0

match rate:
    case 0:
        print("wrong tier selection")
    case _:
        match duration:
            case 1:
                print(1, "hours spent on Tier", computer, ". Current bill =", rate * 1)
            case 2:
                print(1, "hours spent on Tier", computer, ". Current bill =", rate * 1)
                print(2, "hours spent on Tier", computer, ". Current bill =", rate * 2)
            case 3:
                print(1, "hours spent on Tier", computer, ". Current bill =", rate * 1)
                print(2, "hours spent on Tier", computer, ". Current bill =", rate * 2)
                print(3, "hours spent on Tier", computer, ". Current bill =", rate * 3)
            case 4:
                print(1, "hours spent on Tier", computer, ". Current bill =", rate * 1)
                print(2, "hours spent on Tier", computer, ". Current bill =", rate * 2)
                print(3, "hours spent on Tier", computer, ". Current bill =", rate * 3)
                print(4, "hours spent on Tier", computer, ". Current bill =", rate * 4)
            case 5:
                print(1, "hours spent on Tier", computer, ". Current bill =", rate * 1)
                print(2, "hours spent on Tier", computer, ". Current bill =", rate * 2)
                print(3, "hours spent on Tier", computer, ". Current bill =", rate * 3)
                print(4, "hours spent on Tier", computer, ". Current bill =", rate * 4)
                print(5, "hours spent on Tier", computer, ". Current bill =", rate * 5)
            case _:
                print("wrong duration")