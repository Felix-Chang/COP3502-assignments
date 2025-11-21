def fourbonacci(N):
    output = 0

    if N == 1:
        return 1
    elif N == 2:
        return 4
    elif N == 3:
        return 7
    elif N == 4:
        return 8

    f1, f2, f3, f4 = 1, 4, 7, 8

    for i in range(5, N+1):
        f_N = (4 * f1) + (3 * f2) + (2 * f3) + f4
        f1, f2, f3, f4 = f2, f3, f4, f_N
    
    return f4

def odd_squares(n):
    j = -1
    for i in range(n):
       j += 2
       print(j ** 2)
       
def diamond(n):
    for i in range (1, n + 1, 2):
        print(" " * ((n-i) // 2), end = "")
        for j in range(1, i + 1):
            print(j, end = "")
        print()

    for i in range (n-2, 0, -2):
        print(" " * ((n-i) // 2), end = "")
        for j in range(1, i + 1):
            print(j, end = "")
        print()
