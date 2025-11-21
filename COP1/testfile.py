def successor(x):
    return x + 1


def magic(func, x):
    i, total = 1, 0
    while i <= x:
        total, i = total + func(i), i + 1
        print(total)


magic(successor, 5)