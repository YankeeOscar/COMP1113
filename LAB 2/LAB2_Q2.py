
num = float(input("Enter the numerical intelligence: "))
art = float(input("Enter the artistic intelligence: "))

if num > 75 and art > 75:
    print("Label: A")

elif num > 75 and 75 >= art > 50:
    print("Label: B")

elif 75 >= num > 50 and art > 75:
    print("Label: C")

elif 75 >= num > 50 and 75 >= art > 50:
    print("Label: D")

elif 49 > num and 49 > art:
    print("Label: E")

else:
    print("Label: F")
