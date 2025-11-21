import math

def main():
    curr_result = 0.0
    total = 0
    operations_count = 0
    calc_on = True
    display_menu = True

    while calc_on:
        
        if display_menu:
            print(f"Current Result: {curr_result}\n")
            print("Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n")
        
        display_menu = True
        choice = input("\nEnter Menu Selection: ")

        if choice == "0":
            print("Thanks for using this calculator. Goodbye!")
            calc_on = False
        elif choice == "1":
            num1 = input("\nEnter first operand: ")
            num2 = input("Enter second operand: ")

            if num1 == "RESULT":
                num1 = curr_result
            if num2 == "RESULT":
                num2 = curr_result

            curr_result = (float(num1) + float(num2))
            total += curr_result
            operations_count += 1

        elif choice == "2":
            num1 = input("\nEnter first operand: ")
            num2 = input("Enter second operand: ")

            if num1 == "RESULT":
                num1 = curr_result
            if num2 == "RESULT":
                num2 = curr_result

            curr_result = (float(num1) - float(num2))
            total += curr_result
            operations_count += 1

        elif choice == "3":
            num1 = input("\nEnter first operand: ")
            num2 = input("Enter second operand: ")

            if num1 == "RESULT":
                num1 = curr_result
            if num2 == "RESULT":
                num2 = curr_result

            curr_result = (float(num1) * float(num2))
            total += curr_result
            operations_count += 1

        elif choice == "4":
            num1 = input("\nEnter first operand: ")
            num2 = input("Enter second operand: ")

            if num1 == "RESULT":
                num1 = curr_result
            if num2 == "RESULT":
                num2 = curr_result

            curr_result = (float(num1) / float(num2))
            total += curr_result
            operations_count += 1

        elif choice == "5":
            num1 = input("\nEnter first operand: ")
            num2 = input("Enter second operand: ")

            if num1 == "RESULT":
                num1 = curr_result
            if num2 == "RESULT":
                num2 = curr_result

            curr_result = (float(num1) ** float(num2))
            total += curr_result
            operations_count += 1

        elif choice == "6":
            num1 = input("\nEnter first operand: ")
            num2 = input("Enter second operand: ")

            if num1 == "RESULT":
                num1 = curr_result
            if num2 == "RESULT":
                num2 = curr_result

            curr_result = (math.log(float(num2), float(num1)))
            total += curr_result
            operations_count += 1

        elif choice == "7":
            if operations_count != 0:
                print(f"Sum of calculations: {total}")
                print(f"Number of calculations: {operations_count}")
                print(f"Average of calculations: {(total / operations_count):.2f}")
                display_menu = False
            else:
                print("Error: No calculations yet to average!")
                display_menu = False
        else:
            print("Error: Invalid selection!")
            display_menu = False

main()