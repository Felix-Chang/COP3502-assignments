def sum(*nums):
    total = 0.0
    for param in nums:
        total += param

    return total

def print_range(start_num, end_num):
    for i in range(start_num, end_num):
        print(f"{i}, ", end = "")

    print(end_num)

def sum_of_digits(num):
    digits_sum = 0
    for digit in str(num):
        digits_sum += int(digit)
    
    return digits_sum
