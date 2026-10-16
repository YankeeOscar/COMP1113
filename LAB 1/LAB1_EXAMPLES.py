
#Dollar Exchange
'''
dollar = float(input("Enter amount of dollar: "))

EXCHANGE_RATE = 49.13

#Converting dollar to TRY

print(dollar, "$ = ", dollar * EXCHANGE_RATE, "TRY")
'''

#Volume of a Cone

'''
r = float(input("Enter radius of the Cone (cm): "))
h = float(input("Enter height (cm): "))
pi = 3.14159
v = (1/3)*pi*r**2*h
print("The volume of the circle with radius ", r, "is ", v, "cm^3")
'''

#Celsius to Fahrenheit Convert

'''
print("Celsius to Fahrenheit Converter")
C = float(input("Enter Celsius: "))
F = C*1.8+32
print(C, "Celsius equals to:", F, "Fahrenheit")
'''

# Sum of the Numbers

'''
number = int(input("Enter a number between 0 and 999: "))

if number >=100 and number <=999:
    digit1 = number % 10
    digit2 = number // 10
    digit2_1 = digit2 % 10
    digit3 = digit2 // 10
    print(digit1,digit2_1,digit3)
    print("The sum of all intagers is: ", digit1 + digit2_1 + digit3)
    pass

else:
    print("Please enter a number between 0 and 999")
'''