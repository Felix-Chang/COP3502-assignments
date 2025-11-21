initial_principle = float(input("Initial principle: "))
interest_rate = float(input("Interest rate: "))/100 
#divide by 100 to get a decimal value since the input is a %

n = float(input("How many times does interest apply annually: "))
t = float(input("How many years have passed: "))

final_amount = initial_principle * (1 + interest_rate/n) ** (n * t)

print(f"You now have ${final_amount:.2f}")