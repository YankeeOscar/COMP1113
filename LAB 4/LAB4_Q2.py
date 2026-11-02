import math

angle = float(input("Enter the angle in degrees: "))
radian = math.radians(angle)
sin = math.sin(radian)
cos = math.cos(radian)
maximum = max(sin, cos)
result = round(maximum, 4)
print("The result is:", result)