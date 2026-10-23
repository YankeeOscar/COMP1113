"""
    Computer Usage Calculator

    Tool Selection / Per hour usage rate

        Tier A               2  TL
        Tier B               5  TL
        Tier C               10 TL
        Tier D               15 TL

"""

tool = input("Enter the computer tier selection: ")
duration = int(input("Enter reservation duration: "))

match tool:
    case "A":
        rate = 2
        print("Total bill =", duration * rate, "TL")

    case "B":
        rate = 5
        print("Total bill =", duration * rate, "TL")

    case "C":
        rate = 10
        print("Total bill =", duration * rate, "TL")

    case "D":
        rate = 15
        print("Total bill =", duration * rate, "TL")

    case _:
        print("wrong tier selection")