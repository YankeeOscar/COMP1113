t = float(input("Enter today's temperature: ")) #Takes the temperature
m = float(input("Enter money amount in your wallet: ")) # takes the money

if t > 25:
    if m > 100:
        print("Go to the beach BBQ")

    elif 100 >= m > 50:
        print("Go to the beach")

    elif m == 0:
        print("Take a stroll in park")


elif 25 >= t > 15 :
    if m > 100:
        print("Have dinner at a restaurant")

    elif 100 >= m > 50:
        print("Go to cinema")

    elif m == 0:
        print("Watch TV at home")
