item_price = float(input("What is the listed price of the item: "))
paid_amount = float(input("How much did the customer pay: "))

returned_change = paid_amount - item_price * 1.06

print(f"They get ${returned_change:.2f} in change")