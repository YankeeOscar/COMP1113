midterm = float(input("enter the midterm: "))
final = float(input("enter the final: "))
absolute = abs(final - midterm)
maximum = max(final, midterm)
avg = (final + midterm) / 2
result = round(avg)
print("the absolute is: ", absolute)
print("the maximum is: ", maximum)
print("the rounded average is: ", result)
