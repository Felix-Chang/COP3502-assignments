tank_size = float(input("How big is your car's gas tank: "))
current_gallons = float(input("How many gallons are in your tank now: "))
gas_price = float(input("What is the price of gas per gallon: "))

total = (tank_size - current_gallons) * gas_price

print(f"Your gas will cost ${total:.2f}")