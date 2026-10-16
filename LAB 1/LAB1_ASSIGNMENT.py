Jacket = 450
T_Shirt =250
Hat = 200

print("Receipt Executer")

J = int(input("Enter the amount of the Jackets: "))
T = int(input("Enter the amount of the T-Shirts: "))
H = int(input("Enter the amount of the Hats: "))

total = J*Jacket + T*T_Shirt + H*Hat

discount = total * (20/100)
discounted_price = total - discount
print(f"""
    Total price: {total} TL
    Discount amount %20: {discount} TL
    Discounted price {discounted_price} TL
    """
)

payment = float(input("Customer Payment (TL): "))

if payment < discounted_price:
    print("Payment is not enough")
else:
    print("Paid back amount: ", payment-discounted_price, " TL")

print("Github: github.com/YankeeOscar")