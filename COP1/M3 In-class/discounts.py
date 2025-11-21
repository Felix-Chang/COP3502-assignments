# Module 3 In-class Activities

# Discounts

price = float(input("Enter the price: "))
black_friday = input("Is it black friday [y/n]: ")
coupon = input("Do you have a coupon [y/n]: ")
employee = input("Do you have an employee discount [y/n]: ")

if black_friday == "y":
    price *= 0.6
if coupon == "y":
    price *= 0.95
if employee == "y":
    price *= 0.8

print(f"The final price is: ${price:.2f}")