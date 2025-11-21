# Module 3 In-class Activities

# Calculator

operation = input("Enter the operation: ")

operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))

if operation == "add":
    print(f"Result is {(operand1 + operand2):.1f}")
elif operation == "sub":
    print(f"Result is {(operand1 - operand2):.1f}")
elif operation == "mul":
    print(f"Result is {(operand1 * operand2):.1f}")
elif operation == "div":
    print(f"Result is {(operand1 / operand2):.2f}")
    