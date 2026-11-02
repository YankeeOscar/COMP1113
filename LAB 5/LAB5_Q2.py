import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi*math.pow(radius,2)
area_2 = f"{area:.2f}"
print("The area of the circle with radius",radius,"is", area_2)