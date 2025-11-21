def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev = 0
        curr_num = 1

        for i in range(2,n):
            prev, curr_num = (curr_num), (prev + curr_num)
            i += 1
        return curr_num
    
def is_prime(n):

    if n == 1:
        return False
    elif n == 2:
        return True
    elif (n % 2 == 0):
        return False
    for i in range(3, n, 2):
        if (n % i) == 0:
            return False
        i += 1
    return True
        
def print_prime_factors(n):
    if is_prime(n):
        print(f"{n} = {n}")
    else:
        init_num = n
        output = ""
        for i in range (2, n):
            while (n % i == 0):
                if output == "": 
                    output = f"{i}"
                    n /= i
                else:
                    output += f" * {i}"
                    n /= i
            i += 1
        
        print(f"{init_num} = {output}")
