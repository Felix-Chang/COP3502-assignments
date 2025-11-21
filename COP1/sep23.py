def min_terms(n):
    sum = 0
    k = 1
    
    while True:
        sum += (k**k) / (2*k)
        if sum >n:
            return k

# def pattern(n):
#     for i in range(5):
#         for j in range(5):
