def flatten(list_input):
    if not list_input:
        return []
    elif not type(list_input[0]) == list:
        return list_input[0:1] + flatten(list_input[1:])
    elif type(list_input[0]) == list:
        return flatten(list_input[0]) + flatten(list_input[1:])
    
def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5
    while n > 0:
        a, b, c, d, e = b, c, d, e, (a - c + e)
        n -= 1
    return a

def mystery2(number):
    if number == 0:
        return 0
    return (number % 10) + mystery2(number // 10)

def collatz_sequence(n):
    if n <= 1:
        print(1, end=" \n")
    elif (n % 2) == 0:
        print(n, end=" ")
        return collatz_sequence(n//2)
    elif (n % 2) == 1:
        print(n, end=" ")
        return collatz_sequence(3*n + 1)