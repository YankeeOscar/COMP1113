"""
    Electrical Cost Calculator

    Tool Selection / Per hour usage rate

        A               5 kW/h
        B               8 kW/h
        C               12 kW/h
        D               15 kW/h

        1 kW/h costs 5 TL

"""

tool = input("Enter the name of tool: ")
duration = int(input("Enter reservation duration: "))

match tool:
    case "A":
        rate = 5
        print("Total electrical consumption is",duration*rate,"kW/h, cost is",duration*rate*5,"TL")

    case "B":
        rate = 8
        print("Total electrical consumption is",duration*rate,"kW/h, cost is",duration*rate*5,"TL")

    case "C":
        rate = 12
        print("Total electrical consumption is",duration*rate,"kW/h, cost is",duration*rate*5,"TL")

    case "D":
        rate = 15
        print("Total electrical consumption is",duration*rate,"kW/h, cost is",duration*rate*5,"TL")

    case _:
        print("wrong tier selection")