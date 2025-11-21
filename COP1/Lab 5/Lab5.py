def hex_char_decode(digit):
    numbers = "0123456789"
    if digit in numbers:
        return int(digit)
    elif digit.lower() == "a":
        return 10
    elif digit.lower() == "b":
        return 11
    elif digit.lower() == "c":
        return 12
    elif digit.lower() == "d":
        return 13
    elif digit.lower() == "e":
        return 14
    elif digit.lower() == "f":
        return 15

def hex_string_decode(hex):
    if "0x" in hex:
        hex = hex[2:]
    result = 0
    reversed_hex = hex[::-1]

    for i in range(len(hex)):
        numbers = "0123456789"
        if reversed_hex[i] in numbers:
            result += int(reversed_hex[i]) * (16 ** i)
        elif reversed_hex[i].lower() == "a":
            result += 10 * (16 ** i)
        elif reversed_hex[i].lower() == "b":
            result += 11 * (16 ** i)
        elif reversed_hex[i].lower() == "c":
            result += 12 * (16 ** i)
        elif reversed_hex[i].lower() == "d":
            result += 13 * (16 ** i)
        elif reversed_hex[i].lower() == "e":
            result += 14 * (16 ** i)
        elif reversed_hex[i].lower() == "f":
            result += 15 * (16 ** i)
    return result

def binary_string_decode(binary):
    if "0b" in binary:
        binary = binary[2:]
    result = 0
    for i in range(len(binary) - 1, -1, -1):
        result += (2 ** i) * int(binary[len(binary) - 1 - i])
    return result

def binary_to_hex(binary):
    if "0b" in binary:
        binary = binary[2:]
    if (len(binary) % 4) != 0:
        binary = (4 - (len(binary) % 4)) * "0" + binary
        hex = ""
        for i in range(4, len(binary) + 1, 4):
            temp_bin = binary[i-4:i]
            temp_bin = temp_bin[::-1]
            temp_hex = 0
            for j in range(len(temp_bin)):
                temp_hex += (2 ** j) * int(temp_bin[j])
            if temp_hex < 10:
                hex += str(temp_hex)
            elif temp_hex == 10:
                hex += "A"
            elif temp_hex == 11:
                hex += "B"
            elif temp_hex == 12:
                hex += "C"
            elif temp_hex == 13:
                hex += "D"
            elif temp_hex == 14:
                hex += "E"
            elif temp_hex == 15:
                hex += "F"

        leading = True
        new_hex = hex
        for i in range(len(hex)):
            if hex[i] == "0" and leading:
                new_hex = hex[i+1:]
            else:
                leading = False
        return new_hex
    else:
        hex = ""
        for i in range(4, len(binary) + 1, 4):
            temp_bin = binary[i-4:i]
            temp_bin = temp_bin[::-1]
            temp_hex = 0
            for j in range(len(temp_bin)):
                temp_hex += (2 ** j) * int(temp_bin[j])
            if temp_hex < 10:
                hex += str(temp_hex)
            elif temp_hex == 10:
                hex += "A"
            elif temp_hex == 11:
                hex += "B"
            elif temp_hex == 12:
                hex += "C"
            elif temp_hex == 13:
                hex += "D"
            elif temp_hex == 14:
                hex += "E"
            elif temp_hex == 15:
                hex += "F"
        leading = True
        new_hex = hex
        for i in range(len(hex)):
            if hex[i] == "0" and leading:
                new_hex = hex[i+1:]
            else:
                leading = False
        return new_hex
                
if __name__ == "__main__":
    
    while True:
        print("Decoding Menu\n"
              "-------------\n"
              "1. Decode hexadecimal\n"
              "2. Decode binary\n"
              "3. Convert binary to hexadecimal\n"
              "4. Quit\n")
        
        option = input("Please enter an option: ")

        if option == "1":
            number = input("Please enter the numeric string to convert: ")
            print(f"Result: {hex_string_decode(number)}\n")
        elif option == "2":
            number = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_string_decode(number)}\n")
        elif option == "3":
            number = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_to_hex(number)}\n")
        elif option == "4":
            print("Goodbye!")
            break

        while True:
            print("Decoding Menu\n"
                  "-------------\n"
              "1. Decode hexadecimal\n"
              "2. Decode binary\n"
              "3. Convert binary to hexadecimal\n"
              "4. Quit\n")
        
            option = input("Please enter an option: ")

            if option == "1":
                number = input("Please enter the numeric string to convert: ")
                print(f"Result: {hex_string_decode(number)}")
            elif option == "2":
                number = input("Please enter the numeric string to convert: ")
                print(f"Result: {binary_string_decode(number)}")
            elif option == "3":
                number = input("Please enter the numeric string to convert: ")
                print(f"Result: {binary_to_hex(number)}")
            elif option == "4":
                print("Goodbye!")
                break
        break