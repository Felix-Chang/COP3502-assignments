total_income = float(input("Enter your total income this year: "))
owed_taxes = 0

if total_income >= 609_351:
    owed_taxes += (total_income - 609_350) * 0.37
    total_income = 609_350
if total_income >= 243_726:
    owed_taxes += (total_income - 243_725) * 0.35
    total_income = 243_725
if total_income >= 191_951:
    owed_taxes += (total_income - 191_950) * 0.32
    total_income = 191_950
if total_income >= 100_526:
    owed_taxes += (total_income - 100_525) * 0.24
    total_income = 100_525
if total_income >= 47_151:
    owed_taxes += (total_income - 47_150) * 0.22
    total_income = 47_150
if total_income >= 11_601:
    owed_taxes += (total_income - 11_600) * 0.12
    total_income = 11_600
if total_income >= 0:
    owed_taxes += (total_income) * 0.10

print(f"You owe ${owed_taxes:.2f} this year.")