import math

def bin(n):

    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

    return binary

def capitalize(sentence):
    output = ""
    prev_char = None

    for char in sentence:
        if (prev_char == None) or (prev_char == " "):
            prev_char = char
            if char.lower() in "ousnd":
                output += char.lower()
                continue    
            output += char.upper()
        elif char == " ": 
            prev_char = " "
            output += char
        else:
            output += char.lower()
    return output

def partition(numbers, size):
    output = []
    
    for i in range(0, len(numbers), size):
        output.append(numbers[i: i + size])

    return output

    