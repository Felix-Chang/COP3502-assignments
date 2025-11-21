price = float(input("Enter the price of the item: "))
sales_tax = float(input("Enter the sales tax percentage: ")) / 100 # we divide by 100 because the user is inputting a percentage

final_price = price * (1 + sales_tax)

print(f"Your total is ${final_price:.2f}")